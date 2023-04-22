from aiogram import types


async def set_default_commands(dp):

    """Команды для бота по умолчанию"""

    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запустить бота'),
        types.BotCommand('weather', 'Узнать погоду.'),
        types.BotCommand('conversion', 'Конвертация валюты.'),
        types.BotCommand('cute_fox', 'Случайная картинка лисички.'),
        types.BotCommand('survey', 'Создать опрос в группе.'),
        types.BotCommand('help', 'Помощь'),
    ])
