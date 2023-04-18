import json
import requests
from typing import Dict
from loader import OW_API, ERD_API, CURATE_API


def get_weather_data(city: str, lan: str = 'ru', units: str = 'metric') -> Dict:
    """
    Получение данных о погоде в указанном городе.
    :param city: Название города.
    :param lan: Выбор языка для вывода данных.
    :param units: Параметр для меры измерения.
    :return: Словарь с данными о погоде.
    """

    url_api = f'https://api.openweathermap.org/data/2.5/weather?q={city}&lang={lan}&appid={OW_API}&units={units}'
    try:
        response = requests.get(url_api)
        response_json = json.loads(response.text)
        return response_json

    except (Exception, TimeoutError) as _ex:
        print(f'Произошла ошибка {_ex}.')


def get_conversion_data(currency_from: str = 'USD', currency_to: str = 'RUB', amount: float = 1):

    url_api = f"https://api.apilayer.com/exchangerates_data/convert?to=" \
              f"{currency_to}&from={currency_from}&amount={amount}"
    headers = {
        'apikey': ERD_API
    }

    try:
        response = requests.get(url=url_api, headers=headers, data={})
        print(response.text)
    except (Exception, TimeoutError) as _ex:
        print(f'Произошла ошибка {_ex}')


get_conversion_data(amount=5)
