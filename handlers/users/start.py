from aiogram.dispatcher.filters import Command
from aiogram import types
from loader import dp


@dp.message_handler(Command("start"))
async def command_start(message: types.Message) -> None:
    await message.answer(
        f'Здравствуйте {message.from_user.full_name}!\n'
        f'\nЯ помогу вам:\n'
        f'/weather - Узнать погоду в указанном городе.\n'
        f'/conversion - Конвертация валюты.\n'
        f'/cute_animals - Вывод случайной картинки милого животных.\n'
        f'/survey - Создать опрос в группе.'
    )
