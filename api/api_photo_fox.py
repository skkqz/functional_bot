import json
import requests


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
