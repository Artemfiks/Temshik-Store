import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import KeyboardButton, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

import config
from handlers import router


async def main():
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


    router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    InlineKeyboardButton("Перейти", web_app=WebAppInfo('https://habr.com'))
    await msg.answer("Здраствуйте! Вы попали в магазин Temshik Store. Тут вы можете купить всё от Telegram Primium до обучений темкам.")
    InlineKeyboardButton("Перейти", url='https://t.me/<bot_name>?startattach')


@router.message(Command("menu"))
async def menu_handler(msg: Message):
    await msg.answer("Пока")