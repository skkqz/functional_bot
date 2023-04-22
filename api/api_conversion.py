import json
import requests
from typing import Any
from data.config import ERD_API


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

    # Первый запрос к api может долго обрабатываться или получить status_code 500
    response = requests.get(url=url_api, headers=headers, data={})
    response_json = json.loads(response.text)

    if response.status_code != 200:
        return None

    return response_json
