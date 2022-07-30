from main import bot, dp

from aiogram.types import Message
from config import admin_id

from aiogram import types
import os, json, string

async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Бот ишлаябти")

'''**********************************клиентскя част*************************************************'''
@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, 'приятного')

@dp.message_handler(commands=['Режим_работа'])
async def  pizza_open_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Bc-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')

@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Ул А.Навоий 15')
     
'''***********************************Админская ************************************************'''

'''************************************общий ***********************************************'''

@dp.message_handler()
async def echo(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation )) for i in message.text.split(' ')}.intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('мать запрешены')
        await message.delete()