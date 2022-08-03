from aiogram import types, Dispatcher
from main import bot, dp
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sql_data


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, ' Приятного апетита', reply_markup=kb_client)

# @dp.message_handler(commands=['Режим_работа'])
async def  pizza_open_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Bc-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')

# @dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Ул А.Навоий 15', reply_markup=ReplyKeyboardRemove())#reply_markup=ReplyKeyboardRemove() удаляет клавиатуры после нажатие

# @dp.message_handler(lambda message: 'номер' in message.text)
async def number(message: types.Message):
    await message.answer('Номер админа +996555706470')

# @dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message: types.Message):
    await sql_data.sql_read(message)
       

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start,commands=('start', 'help'))
    dp.register_message_handler(pizza_open_command,commands=('Режим_работы'))
    dp.register_message_handler(pizza_place_command,commands=('Расположение'))
    dp.register_message_handler(number, lambda message: 'номер' in message.text)
    dp.register_message_handler(pizza_menu_command, commands=('Меню'))
