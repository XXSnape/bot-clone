import asyncio

from aiogram.types import CallbackQuery

from core.texts import WAIT_FOR_TEXT
from keyboards.inline.menu import go_to_menu_kb
from utils.tg import delete_message


async def send_text(callback: CallbackQuery, text: str):
    await delete_message(callback.message)
    msg = await callback.message.answer(WAIT_FOR_TEXT)
    await asyncio.sleep(0.1)
    await msg.edit_text(text, reply_markup=go_to_menu_kb())
