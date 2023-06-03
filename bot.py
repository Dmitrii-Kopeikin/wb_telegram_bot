import asyncio

from telebot.async_telebot import AsyncTeleBot

from wb_bot.handlers import find_item_position_handler, start_handler
from config import config


def register_handlers(bot: AsyncTeleBot):
    bot.register_message_handler(start_handler.start_handler, commands=[
                                 'start'], pass_bot=True)
    bot.register_message_handler(
        # find_item_position_handler.find_item_position, commands=['message'], pass_bot=True)
        find_item_position_handler.find_item_position, content_types=['text'], pass_bot=True)


async def run():
    bot = AsyncTeleBot(config.TOKEN)
    register_handlers(bot)
    await bot.polling(non_stop=True)


asyncio.run(run())
