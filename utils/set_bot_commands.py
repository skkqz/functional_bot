from aiogram import types


async def set_default_commands(dp):

    """Команды для бота по умолчанию"""

    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запустить бота'),
        types.BotCommand('weather', 'Конвертация валюты.'),
        types.BotCommand('conversion', 'Конвертация валюты.'),
        types.BotCommand('cute_fox', 'Вывод случайной картинки милого животных.'),
        types.BotCommand('survey', 'Создать опрос в группе.'),
        types.BotCommand('help', 'Помощь'),
    ])
