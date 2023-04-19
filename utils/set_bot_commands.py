from aiogram import types


async def set_default_commands(dp):

    """Команды для бота по умолчанию"""

    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запустить бота'),
        types.BotCommand('help', 'Помощь'),
    ])
