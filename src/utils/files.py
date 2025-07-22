import asyncio

from aiogram.types import CallbackQuery

from core.texts import WAIT_FOR_TEXT
from keyboards.inline.menu import go_to_menu_kb
from utils.tg import delete_message, get_fsinput_file


async def send_file(callback: CallbackQuery, filename: str, caption: str):
    await delete_message(callback.message)
    file = get_fsinput_file(filename)
    msg = await callback.message.answer(WAIT_FOR_TEXT)
    await asyncio.sleep(0.2)
    await msg.delete()
    await callback.message.answer_document(
        file,
        caption=caption,
        reply_markup=go_to_menu_kb(),
    )
