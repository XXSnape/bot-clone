from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.builder import generate_inline_kb
from .common import get_common_buttons


def c1_options() -> InlineKeyboardMarkup:
    return generate_inline_kb(
        data_with_buttons=[
            InlineKeyboardButton(
                text="Создание Заказа Покупателя и выставление счета",
                callback_data="create_order",
            ),
            InlineKeyboardButton(
                text="Создание отгрузочной накладной", callback_data="create_shipment"
            ),
            InlineKeyboardButton(
                text="Возврат от покупателя", callback_data="customer_return"
            ),
            InlineKeyboardButton(
                text="Создание контрагента", callback_data="create_counterparty"
            ),
            InlineKeyboardButton(
                text="Создание номенклатуры", callback_data="create_nomenclature"
            ),
            *get_common_buttons(),
        ]
    )
