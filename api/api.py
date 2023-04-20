import json
import requests
from typing import Dict, Any
from data.config import OW_API, ERD_API


def get_weather_data(city: str, lan: str = 'ru', units: str = 'metric') -> Dict:
    """
    Получение данных о погоде в указанном городе.
    :param city: Название города.
    :param lan: Выбор языка для вывода данных.
    :param units: Параметр для меры измерения.
    :return: Словарь с данными о погоде.
    """

    url_api = f'https://api.openweathermap.org/data/2.5/weather?q={city}&lang={lan}&appid={OW_API}&units={units}'
    response = requests.get(url_api)
    response_json = json.loads(response.text)

    return response_json


def get_conversion_data(currency_from: str = 'USD', currency_to: str = 'RUB', amount: float = 1) -> Any:
    """
    Получение конвертации валюты
    :param currency_from: Из какой валюты.
    :param currency_to: В какую валюту.
    :param amount: Сумма конвертации
    :return: Словарь с данными конвертации
    """

    url_api = f"https://api.apilayer.com/exchangerates_data/convert?to=" \
              f"{currency_to}&from={currency_from}&amount={amount}"
    headers = {
        'apikey': ERD_API
    }

    # Первый запрос к api может долго обрабатываться или получить ошибку 500
    response = requests.get(url=url_api, headers=headers, data={})
    response_json = json.loads(response.text)

    if response.status_code != 200:
        return None

    return response_json


def get_photo_fox():

    """
    Api для генерации случайного фото лисички.
    :return: Список с url ссылкой фото лисички
    """
    # Выбрал этот api вместо хранения фотографий милых животных в репозитории

    url_api = 'https://randomfox.ca/floof/'
    response = requests.get(url_api)
    response_json = json.loads(response.text)

    return response_json
