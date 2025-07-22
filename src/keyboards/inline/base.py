from aiogram.types import InlineKeyboardButton

from keyboards.inline.builder import generate_inline_kb
from keyboards.inline.common import get_common_buttons


def base_options():
    return generate_inline_kb(
        [
            InlineKeyboardButton(
                text="Барный инвентарь", callback_data="bar_inventory"
            ),
            InlineKeyboardButton(
                text="Сиропы, топинги, пюре", callback_data="syrups_toppings"
            ),
            InlineKeyboardButton(text="Оборудование", callback_data="equipment"),
            *get_common_buttons(),
        ]
    )
