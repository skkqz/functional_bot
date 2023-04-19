from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp
from api.api import get_conversion_data
from states.data_collections import DataCollection


@dp.message_handler(Command('conversion'))
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
        test = await message.answer(text='Пожалуйста подождите...')
        message_int = int(message.text)
        async with state.proxy() as data:
            data['conversion_amount'] = message_int

            result = get_conversion_data(
                currency_from=data['conversion_from'],
                currency_to=data['conversion_to'],
                amount=data['conversion_amount']
            )
            print(result)
            await test.delete()
    except Exception as _ex:
        await message.answer('Введены не верные данные. Проверьте правильность введённых данных и повторите запрос.')
        print(f'Ошибка {_ex}')
    finally:
        await state.finish()
