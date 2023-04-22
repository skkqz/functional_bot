from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Создание inline клавиатуры для повторного вывода фото пользователю
choice = InlineKeyboardMarkup()
btn_more = InlineKeyboardButton(text='Может быть еще фото? 😊', callback_data='more')
choice.add(btn_more)
