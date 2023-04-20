from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from data.config import ID_GROUP
from states.data_poll_group import DataPoolGroup
from loader import dp, bot, logger


# @dp.message_handler(Command('survey'))
# async def command_poll_group(message: types.Message) -> None:
#     """
#
#     :param message:
#     :return:
#     """
#
#     await message.answer('Опачки')
#     await bot.send_poll(chat_id=ID_GROUP,
#                         question='тестовый порос',
#                         options=['1', '2', '3'],
#                         correct_option_id=1,
#                         is_anonymous=True
#                         )


@dp.message_handler(Command('survey'))
async def command_poll_group(message: types.Message) -> None:
    """Получаем от пользователя вопрос для опроса"""

    await message.answer('Пожалуйста введите вопрос для опроса.')
    await DataPoolGroup.question.set()


@dp.message_handler(state=DataPoolGroup.question)
async def poll_group_question(message: types.Message, state: FSMContext):
    """Получаем от пользователя список ответов"""

    async with state.proxy() as data:
        data['question'] = message.text
        data['list_of_options'] = list()


    await message.answer('Пожалуйста введите варианты ответов через пробел.')
    await DataPoolGroup.next()


@dp.message_handler(state=DataPoolGroup.list_of_options)
async def poll_group_list_of_options(message: types.Message, state: FSMContext):
    """Получаем от пользователя номер правильного ответа"""

    async with state.proxy() as data:

        data['list_of_options'].append(message.text)
        print(data)

        if len(data['list_of_options']) < 2:
            await poll_group_question(message, state)

    await message.answer('Пожалуйста введите номер правильного ответа'
                         '\nПример: 1 (В таком случае правильный ответ будет Вопрос_1)')
    await DataPoolGroup.next()


@dp.message_handler(state=DataPoolGroup.correct_answer)
async def poll_group_correct_answer(message: types.Message, state: FSMContext):
    """Получаем от пользователя ответ будет ли опрос анонимным"""

    async with state.proxy() as data:
        data['correct_answer'] = message.text

    await message.answer('Опрос будет анонимным? Да/Нет.')
    await DataPoolGroup.next()


@dp.message_handler(state=DataPoolGroup.is_anonymous)
async def poll_group_is_anonymous(message: types.Message, state: FSMContext):
    """Получаем от пользователя номер правильного ответа"""

    try:
        async with state.proxy() as data:
            if message.text.lower() == 'да':
                data['is_anonymous'] = True
            else:
                data['is_anonymous'] = False

            print(data)
            await bot.send_poll(chat_id=ID_GROUP,
                                question=data['question'],
                                options=data['list_of_options'],
                                correct_option_id=int(data['correct_answer']) - 1,
                                is_anonymous=data['is_anonymous']
                                )

    except (Exception, TimeoutError) as _ex:
        await message.answer('Произошла непредвиденная ошибка. Проверьте введённые данные или повторите запрос позже.')
        logger.error(f'Ошибка: {_ex}')
    finally:
        await state.finish()
