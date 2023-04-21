from aiogram.dispatcher.filters.state import State, StatesGroup


# Класс для хранения данных от пользователя
class DataPoolGroup(StatesGroup):
    """
    Сбор данных для опроса в группе
    """

    question = State()
    list_of_options = State()
    is_anonymous = State()
