from aiogram.types import InlineKeyboardButton

from keyboards.inline.builder import generate_inline_kb
from keyboards.inline.common import get_common_buttons

BACK_BTN = InlineKeyboardButton(text="<< Назад", callback_data="enclosure")


def enclosure_options():
    return generate_inline_kb(
        [
            InlineKeyboardButton(text="Первый", callback_data="first"),
            InlineKeyboardButton(
                text="Воторой",
                callback_data="final",
            ),
            InlineKeyboardButton(
                text="третий",
                callback_data="third",
            ),
            *get_common_buttons(),
        ]
    )


def first_kb():
    return generate_inline_kb(
        [
            InlineKeyboardButton(text="ПодПодКатегория", callback_data="sub_category"),
            InlineKeyboardButton(
                text="2 ПодПодКатегория",
                callback_data="final",
            ),
            BACK_BTN,
            *get_common_buttons(with_back=False),
        ]
    )


def sub_category_kb():
    return generate_inline_kb(
        [
            InlineKeyboardButton(text="Еще вложеннее", callback_data="final"),
            BACK_BTN,
            *get_common_buttons(with_back=False),
        ]
    )
