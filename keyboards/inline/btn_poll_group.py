from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choice = InlineKeyboardMarkup()
is_anonymous_yes = InlineKeyboardButton(text='Анонимно', callback_data='is_anonymous_yes')
is_anonymous_no = InlineKeyboardButton(text='публичный', callback_data='is_anonymous_no')
choice.add(is_anonymous_yes, is_anonymous_no)
