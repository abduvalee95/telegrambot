from aiogram.types import Message
from config import admin_id
from main import bot, dp
from data_base import sql_data


async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Бот ишлаябти")
    sql_data.sql_start()

from handler import client, admin, other

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)