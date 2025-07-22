from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.builder import generate_inline_kb
from keyboards.inline.common import get_common_buttons


def complaints_options() -> InlineKeyboardMarkup:
    return generate_inline_kb(
        [
            InlineKeyboardButton(text="Клен", callback_data="klen"),
            InlineKeyboardButton(
                text="Рестинтернешни", callback_data="restinternational"
            ),
            InlineKeyboardButton(text="Мастергласс", callback_data="masterglass"),
            InlineKeyboardButton(
                text="Регион 50 (Проект 2015)", callback_data="region50"
            ),
            InlineKeyboardButton(
                text="Русский проект (Метроном)", callback_data="russian_project"
            ),
            *get_common_buttons(),
        ]
    )
