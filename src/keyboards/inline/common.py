from aiogram.types import InlineKeyboardButton

from keyboards.inline.builder import generate_inline_kb

MENU_CB = "menu"
TO_MENU_BTN = InlineKeyboardButton(text="В меню ↩️", callback_data=MENU_CB)
TO_BACK_BTN = InlineKeyboardButton(text="<< Назад", callback_data=MENU_CB)


def get_common_buttons(with_back: bool = True) -> tuple[InlineKeyboardButton, ...]:
    if with_back:
        return TO_BACK_BTN, TO_MENU_BTN
    return (TO_MENU_BTN,)
