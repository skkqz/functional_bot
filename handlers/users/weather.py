from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp
from api.api import get_weather_data
from states.data_collections import DataCollection


@dp.message_handler(Command('weather'))
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
