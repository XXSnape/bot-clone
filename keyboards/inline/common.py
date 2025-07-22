from aiogram.types import InlineKeyboardButton

MENU_CB = "menu"
TO_MENU_BTN = InlineKeyboardButton(text="В меню ↩️", callback_data=MENU_CB)
TO_BACK_BTN = InlineKeyboardButton(text="<< Назад", callback_data=MENU_CB)


def get_common_buttons() -> tuple[InlineKeyboardButton, ...]:
    return (TO_MENU_BTN, TO_BACK_BTN)
