from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from .builder import generate_inline_kb
from .common import get_common_buttons


MENU_CB = "menu"


def menu_kb() -> InlineKeyboardMarkup:
    return generate_inline_kb(
        [
            InlineKeyboardButton(text="1С", callback_data="1с"),
            InlineKeyboardButton(text="Рекламации", callback_data="complaints"),
            InlineKeyboardButton(text="База знаний", callback_data="check"),
            InlineKeyboardButton(
                text="Сервисное обслуживание оборудования", callback_data="service"
            ),
            InlineKeyboardButton(text="О компании", callback_data="company"),
            InlineKeyboardButton(
                text="Проверка вложенности", callback_data="enclosure"
            ),
            InlineKeyboardButton(text="Техническая поддержка", callback_data="support"),
        ]
    )


def go_to_menu_kb():
    return generate_inline_kb(get_common_buttons(with_back=False))
