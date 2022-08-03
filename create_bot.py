from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from config import BOT_TOKEN
from aiogram import types

# dp = Dispatcher(bot)
# # это для прмер 

# @dp.message_handler(commands=['start', 'help'])
# async def command_start(message: types.Message):
#     await message.reply('Ассалому алайкум')

# @dp.message_handler(lambda message: 'такси' in message.text )
# async def taxi(message : types.Message):
#     # здесь добавляется базаданных бот  реагирует на слово такси 
#     await message.answer(message.text)

# @dp.message_handler(lambda message: 'нло' in message.text )
# async def ufo(message : types.Message):
#     await message.answer('нлоооо')

# @dp.message_handler(command=['команда'])
# async def echo(message : types.Message):
#     await message.answer('message.text')

# @dp.message_handler()
# async def empty(message : types.Message):
#     await message.answer('Нет такой команда')
#     await message.delete()