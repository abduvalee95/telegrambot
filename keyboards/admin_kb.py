from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


#Кнопки Админ
button_load = KeyboardButton('/Загрузить')
button_delete = KeyboardButton('/Удалить')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).row(button_load).row(button_delete)