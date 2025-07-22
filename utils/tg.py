from contextlib import suppress
from pathlib import Path

from aiogram.exceptions import TelegramAPIError
from aiogram.types import Message, InlineKeyboardMarkup


async def delete_message(message: Message) -> None:
    with suppress(Exception):
        await message.delete()


async def edit_message_or_write_new(
    message: Message,
    text: str,
    markup: InlineKeyboardMarkup | None,
):
    try:
        await message.edit_text(text=text, reply_markup=markup)
    except TelegramAPIError:
        await message.answer(text=text, reply_markup=markup)


def get_fsinput_file(filename: str):
    path = Path(__file__).parent.parent / "files" / filename
