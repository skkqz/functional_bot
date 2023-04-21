from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.config import BOT_API
from loguru import logger

bot = Bot(token=BOT_API, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

logger.add('logging/logging_error.log', format="{time}|{level}|{name}|{message}",
           level='ERROR', encoding='utf-8', rotation='5 MB')
