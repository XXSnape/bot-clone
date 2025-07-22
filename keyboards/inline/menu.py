from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from .builder import generate_inline_kb


def menu_kb() -> InlineKeyboardMarkup:
    return generate_inline_kb(
        [
            InlineKeyboardButton(text="1С", callback_data="1с"),
            InlineKeyboardButton(text="Рекламации", callback_data="сomplaints"),
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


MENU_CB = "menu"
