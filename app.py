from aiogram import executor
from utils.set_bot_commands import set_default_commands
from handlers import dp
from loader import logger


async def on_startup(dp):

    await set_default_commands(dp)
    logger.info('Бот включен')


if __name__ == '__main__':

    """Запуск бота в работу """

    executor.start_polling(dp, on_startup=on_startup)
