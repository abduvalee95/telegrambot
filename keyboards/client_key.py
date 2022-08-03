from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/Режим_работы') 
b2 = KeyboardButton('/Расположение') 
b3 = KeyboardButton('/Меню')
b4 = KeyboardButton('Поделиться контакт',request_contact=True)
b5 = KeyboardButton('Отправить свой местоположение',request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True) #one_time_keyboard=True автоматический спрятатса клавиатура

# kb_client.add(b1).add(b2).add(b3)#расположение клавиатуры 1
kb_client.add(b1).add(b2).insert(b3).add(b4).add(b5)#расположение клавиатуры 1
# kb_client.row(b1,b2,b3)#расположение клавиатуры 1
# kb_client.add(b1).row(b2).insert(b3)
