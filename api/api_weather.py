import json
import requests
from typing import Dict
from data.config import OW_API


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
