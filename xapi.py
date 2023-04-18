import json
import requests
from typing import Dict
from loader import OW_API


def get_weather_data(name_city: str, lan: str = 'ru', units: str = 'metric'):
    """
    Получение данных о погоде в указанном городе.
    :param name_city: Название города.
    :param lan: Выбор языка для вывода данных.
    :param units: Параметр для меры измерения.
    :return: Словарь с данными о погоде.
    """

    url_api = f'https://api.openweathermap.org/data/2.5/weather?q={name_city}&lang={lan}&appid={OW_API}&units={units}'
    response = requests.get(url_api)
    print(response.text)


get_weather_data('Тверь')