from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from data.config import ADMIN


class IsAdmin(BoundFilter):
    """Фильтр для пользования ботом только администратором"""

    # Фильтр для ограничения некоторых команд пользователю. Где указан этот фильтр команда доступна
    # только администраторам
    async def check(self, message: types.Message):
        if str(message.from_user.id) in ADMIN:
            return True
        else:
            await message.answer('У вас нету доступа к командам бота')
            return False
