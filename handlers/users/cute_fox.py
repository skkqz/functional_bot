from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from loader import dp, logger
from api.api import get_photo_fox
from keyboards.inline.btn_more import choice


@dp.message_handler(Command('cute_fox'))
async def command_cute_fox(message: types.Message) -> None:
    """Вывод случайной фотографии лисички"""

    try:
        result = get_photo_fox()
        await message.answer_photo(photo=result['image'], caption='🦊😍', reply_markup=choice)
    except (Exception, TimeoutError) as _ex:
        await message.answer('Произошла непредвиденная ошибка. Повторите запрос позже.')
        logger.error(f'Ошибка: {_ex}')


@dp.callback_query_handler(text_contains='more')
async def more_photo_fox(call: CallbackQuery) -> None:

    """Обработка нажатой inline клавиатуры"""

    # Удаляет inline кнопку, находящуюся в предыдущем сообщении
    await call.message.delete_reply_markup()
    await command_cute_fox(call.message)
