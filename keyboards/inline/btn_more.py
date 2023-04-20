from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choice = InlineKeyboardMarkup()
btn_more = InlineKeyboardButton(text='Может быть еще фото? 😊', callback_data='more')
choice.add(btn_more)
