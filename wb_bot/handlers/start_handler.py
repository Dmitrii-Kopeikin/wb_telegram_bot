from telebot import TeleBot
from telebot.types import Message


async def start_handler(message: Message, bot: TeleBot):
    text = (
        "Привет. Я могу найти позицию в поисковой выдаче WB по артикулу.\n"
        "Просто введи запрос и артикул.\n"
        "Например: \n"
        "    велосипед детский 145296859"
    )
    await bot.send_message(message.chat.id, text)
