import asyncio

from telebot import TeleBot
from telebot.types import Message

from wb_scrapper.find_position_by_art import get_good_position, prepare_url


async def worker(query: str, art: str, message: Message, bot: TeleBot):
    result = await get_good_position(query, art)
    if result[0] != -1:
        page, position, absolute_position = result
        answer = (f'Артикул: {art}\n'
                  f'Страница: {page}, Позиция: {position}\n'
                  f'Абсолютная позиция: {absolute_position}\n'
                  f'Ссылка: {prepare_url(query, page)}')
        await bot.reply_to(message, answer)
        return

    await bot.reply_to(message, f'Артикул {art} не найден по данному запросу.')


async def find_item_position(message: Message, bot: TeleBot):
    if len(message.text.split()) < 2:
        await bot.reply_to(message, 'Не верный запрос.')
        return

    *query, art = message.text.split()
    query = '%20'.join(query)

    await bot.reply_to(message, 'В обработке...')
    asyncio.create_task(worker(query, art, message, bot))
