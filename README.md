<div align="center">
<img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/>
<img alt="Telegram" src="https://img.shields.io/badge/Telegram-blue?&style=for-the-badge&logoColor=white&logo=telegram"/>
<img alt="PyCharm" src="https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white"/>
<img alt="Git" src="https://img.shields.io/badge/git-%23F05033.svg?&style=for-the-badge&logo=git&logoColor=white"/>
</div>

# Много функциональный Telegram бот

Это многофункциональный Telegram бот, который может выполнять различные задачи, такие как проверка погоды в указанном
городе, конвертация валюты, отправка милых фото лисичек и создание опросов в групповом чате.

## Подготовка к запуску бота

### Клонировать репозиторий 

* Клонируйте этот репозиторий с помощью команды: `git clone https://github.com/skkqz/functional_bot.git`

### Установите все зависимости

* Python 3.7 +
* aiogram 2.25.1
* loguru 0.7.0
* python-dotenv 1.0.0
* requests 2.28.2
* Вы можете установить все зависимости одной командой: `pip install -r requirements.txt`

### Настройка  .env

* Для работы бота вам нужно создать файл .env в корневой директории проекта и вставить следующие ключи и значения:

```
BOT_API=Ваш токен бота
OW_API=Ваш ключ OpenWeatherMap API
ERD_API=Ваш ключ Exchange Rates API
ID_GROUP=Ваш id группы
ADMIN=Ваш id
```
* Получите token бота у [@BotFather](https://t.me/BotFather)
* Получить ключ для [OpenWeatherMap API](https://openweathermap.org/api)
* Получить ключ для [Exchange Rates API](https://apilayer.com/marketplace/exchangerates_data-api#pricing)
* Узнайте id вашей группы в Telegram с помощью бота [@username_to_id_bot](https://t.me/username_to_id_bot) 
* Узнайте свой id в Telegram с помощью бота [@getmyid_bot](https://t.me/getmyid_bot)

## Запуск бота

* Для запуска бота выполните следующую команду: `python app.py`

## Команды

Для бота доступны следующие команды:

* /weather - Получить погоду в указанном городе.
* /conversion - Конвертировать валюту по текущему курсу.
* /cute_fox - Получить случайное милое фото лисички.
* /survey - Создать опрос в текущем групповом чате.

### Участники проекта
* [skkqz](https://github.com/skkqz)

Вы можете внести свой вклад в этот проект, создавая issues или pull requests.