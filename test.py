from data.config import BOT_API
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from xapi import get_weather_data, get_conversion_data

bot = Bot(token=BOT_API)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)


class DataCollection(StatesGroup):
    """
    Сбор данных от пользователя
    """
    city = State()
    conversion_from = State()
    conversion_to = State()
    conversion_amount = State()


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer(
        f'Здравствуйте {message.from_user.full_name}!\n'
        f'\nЯ помогу вам:\n'
        f'/weather - Узнать погоду в указанном городе.\n'
        f'/conversion - Конвертация валюты.\n'
        f'/cute_animals - Вывод случайной картинки милого животных.\n'
        f'/survey - Создать опрос в группе.'
    )


@dp.message_handler(commands=['weather'])
async def cmd_weather(message: types.Message) -> None:
    """Запрос у пользователя название города в котором нужно получить погодные условия"""

    await message.answer(text='Введите название города:')
    await DataCollection.city.set()


@dp.message_handler(state=DataCollection.city)
async def get_weather(message: types.Message, state: FSMContext) -> None:
    """Вывод пользователю данных о погоде в городе."""

    try:
        city = message.text
        get_result = get_weather_data(city)

        # Проверю, что api отдал данные с кодом 200, если код другой
        if get_result.get('cod') == 200:

            text_result = f'{get_result["name"]} {round(get_result["main"]["temp"])}°C\n' \
                          f'{get_result["weather"][0]["description"].capitalize()}\n' \
                          f'Влажность: {get_result["main"]["humidity"]}%\n' \
                          f'Ветер: {round(get_result["wind"]["speed"])} м/с'

            await message.answer(text=text_result)
        else:
            await message.answer(text=f'Указанный город не найден. Проверьте введённые данные.')

    except Exception as _ex:
        await message.answer(text='Произошла не предвиденная ошибка. Пожалуйста повторите запрос позже.')
        print(f'Произошла неожиданная ошибка {_ex}')
    finally:
        await state.finish()


@dp.message_handler(commands=['conversion'])
async def cmd_conversion(message: types.Message) -> None:
    """Запрос у пользователя какую валют нужно конвертировать"""

    await message.answer(text='Введите какую валюту нужно конвертировать:\nПример: USD')
    await DataCollection.conversion_from.set()


@dp.message_handler(state=DataCollection.conversion_from)
async def get_conversion_form(message: types.Message, state: FSMContext):
    """Запрос у пользователя из какой валюты нужно будет конвертировать"""

    async with state.proxy() as data:
        data['conversion_from'] = message.text

    await message.answer(text='Введите в какую валюту нужно конвертировать:\nПример: RUB')
    await DataCollection.next()


@dp.message_handler(state=DataCollection.conversion_to)
async def get_conversion_amount(message: types.Message, state: FSMContext):
    """Запрос у пользователя количество валюты для конвертации"""

    async with state.proxy() as data:
        data['conversion_to'] = message.text

    await message.answer(text='Введите количество валюты для конвертации:\nПример (должно быть число): 1')
    await DataCollection.next()


@dp.message_handler(state=DataCollection.conversion_amount)
async def get_conversion_amount(message: types.Message, state: FSMContext):
    """Получение данных от пользователя количество валюты для конвертации"""

    try:

        message_int = int(message.text)
        async with state.proxy() as data:
            data['conversion_amount'] = message_int

            result = get_conversion_data(
                currency_from=data['conversion_from'],
                currency_to=data['conversion_to'],
                amount=data['conversion_amount']
            )
            print(result)
    except Exception as _ex:
        await message.answer('Введены не верные данные. Проверьте правильность введённых данных и повторите запрос.')
        print(f'Ошибка {_ex}')
    finally:
        await state.finish()


if __name__ == '__main__':
    print('Бот включен')
    executor.start_polling(dp, skip_updates=True)
