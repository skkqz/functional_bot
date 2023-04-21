from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils import exceptions

from data.config import ID_GROUP
from states.data_poll_group import DataPoolGroup
from loader import dp, bot, logger
from filters.ia_admin import IsAdmin
from keyboards.inline.btn_poll_group import choice


# IsAdmin() Моя логика тут в том, чтобы ограничить пользователей группы в командах бота. По желанию это можно
# настроить для любой команды.
# Тут я использовал машинное состояние FSMContext для того, чтобы хранить в переменных нужные мне данные и
# передавать их из хендлера в хендлер.
@dp.message_handler(Command('survey'), IsAdmin())
async def command_survey(message: types.Message) -> None:

    """Команда запускает событие для создания опроса в группе."""

    await message.answer('Какой будет опрос?', reply_markup=choice)


@dp.message_handler(state=DataPoolGroup.question)
async def survey_question(message: types.Message, state: FSMContext) -> None:

    """Сохраняем вопрос. Запрашиваем у пользователя список ответов."""

    async with state.proxy() as data:
        data['question'] = message.text
    await message.answer('Введите пожалуйста варианты ответов разделя их ";" (Должно быть минимум 2 вопроса).')
    await DataPoolGroup.next()


@dp.message_handler(state=DataPoolGroup.list_of_options)
async def survey_list_of_options(message: types.Message, state: FSMContext) -> None:

    """Сохраняем список ответов. Выводим результат пользователю."""

    try:
        async with state.proxy() as data:
            data['list_of_options'] = message.text.split(';')
            await bot.send_poll(chat_id=ID_GROUP,
                                question=data['question'],
                                options=data['list_of_options'],
                                is_anonymous=data['is_anonymous'],
                                )
            await message.answer('Опрос был удачно создан')
    except (Exception, exceptions.PollError) as _ex:
        logger.error(f'Ошибка: {_ex}')
        await message.answer('Пожалуйста проверьте введённые данные и повторите команду')
    finally:
        await state.finish()


@dp.callback_query_handler(lambda call: call.data.startswith('is_anonymous'))
async def callback_is_anonymous(call: CallbackQuery, state: FSMContext) -> None:

    """Обработка inline клавиатуры. Сохраняем ответ."""

    await call.message.delete_reply_markup()
    async with state.proxy() as data:
        if call.data == 'is_anonymous_yes':
            data['is_anonymous'] = True
        else:
            data['is_anonymous'] = False

    await call.message.answer('Напишите вопрос: ')
    await DataPoolGroup.question.set()
