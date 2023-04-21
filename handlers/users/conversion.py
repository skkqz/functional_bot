from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp, logger
from api.api_conversion import get_conversion_data
from states.data_collections import DataCollection


# Тут я также использовал FSMContext для хранения нужной информации от пользователя.
# Собрал нужные данные от пользователя для апи, передал их в get_conversion_data(), вывел пользователю результат или
# текст ошибки.
@dp.message_handler(Command('conversion'))
async def cmd_conversion(message: types.Message) -> None:

    """Запрос у пользователя какую валют нужно конвертировать"""

    await message.answer(text='Введите какую валюту нужно конвертировать:\nПример: USD')
    await DataCollection.conversion_from.set()


@dp.message_handler(state=DataCollection.conversion_from)
async def get_conversion_form(message: types.Message, state: FSMContext) -> None:

    """Запрос у пользователя из какой валюты нужно будет конвертировать"""

    async with state.proxy() as data:
        data['conversion_from'] = message.text

    await message.answer(text='Введите в какую валюту нужно конвертировать:\nПример: RUB')
    await DataCollection.next()


@dp.message_handler(state=DataCollection.conversion_to)
async def get_conversion_to(message: types.Message, state: FSMContext) -> None:

    """Запрос у пользователя количество валюты для конвертации"""

    async with state.proxy() as data:
        data['conversion_to'] = message.text

    await message.answer(text='Введите количество валюты для конвертации:\nПример (должно быть число): 1')
    await DataCollection.next()


@dp.message_handler(state=DataCollection.conversion_amount)
async def get_conversion_amount(message: types.Message, state: FSMContext) -> None:

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

            if result is not None:
                """Вывод результата конвертации валюты"""

                await test.delete()
                text_result = f'Курс на {result["date"]} - ' \
                              f'{round(result["info"]["rate"], 2)} {result["query"]["to"]}\n' \
                              f'{result["query"]["amount"]} {result["query"]["from"]}' \
                              f' = {round(result["result"], 2)} {result["query"]["to"]}'
                await message.answer(text=text_result)
            else:
                await message.answer('Введены не верные данные.'
                                     ' Проверьте правильность введённых данных и повторите запрос.')
                await test.delete()
    except (Exception, TimeoutError) as _ex:
        await message.answer('Произошла непредвиденная ошибка. Повторите запрос позже.')
        logger.error(f'Ошибка: {_ex}')
    finally:
        await state.finish()
