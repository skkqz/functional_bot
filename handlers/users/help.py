from aiogram.dispatcher.filters import Command
from aiogram import types
from loader import dp


@dp.message_handler(Command('help'))
async def command_help(message: types.Message) -> None:
    await message.answer(
        f'Помощь по командам:\n'
        f'/weather - Узнать погоду в указанном городе.\n'
        f'/conversion - Конвертация валюты.\n'
        f'/cute_fox - Вывод случайной картинки милого животных.\n'
        f'/survey - Создать опрос в группе.'
    )
