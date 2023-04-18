from loader import BOT_API

from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(BOT_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.reply(f'Привет {message.from_user.full_name}')


if __name__ == '__main__':
    print('Бот включен')
    executor.start_polling(dp, skip_updates=True)
