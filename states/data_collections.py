from aiogram.dispatcher.filters.state import State, StatesGroup


# Класс для хранения данных от пользователя
class DataCollection(StatesGroup):
    """
    Сбор данных от пользователя
    """
    city = State()
    conversion_from = State()
    conversion_to = State()
    conversion_amount = State()
