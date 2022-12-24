import asyncio

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import BOT_TOKEN, list_channels
from aiogram.types import Message

from aiogram import types


storage = MemoryStorage()
loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode='HTML', disable_web_page_preview=True)
dp = Dispatcher(bot, storage=storage, loop=loop)


@dp.chat_join_request_handler()
async def join(update: types.ChatJoinRequest):
    if update.chat.id in list_channels:
        await update.approve()


def start_bot():
    executor.start_polling(dp)

start_bot()