from aiogram.dispatcher.filters.state import State, StatesGroup


class DataPoolGroup(StatesGroup):
    """
    Сбор данных для опроса в группе
    """

    question = State()
    list_of_options = State()
    correct_answer = State()
    is_anonymous = State()
