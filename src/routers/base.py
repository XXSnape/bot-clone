from aiogram import Router, F
from aiogram.types import CallbackQuery

from core.texts import WAIT_FOR_TEXT
from keyboards.inline.base import base_options
from utils.files import send_file
from utils.tg import edit_message_or_write_new, delete_message

router = Router(name=__name__)


@router.callback_query(F.data == "check")
async def get_options(callback: CallbackQuery):
    await edit_message_or_write_new(
        message=callback.message, text="Выберите подкатегорию", markup=base_options()
    )


@router.callback_query(F.data == "bar_inventory")
async def bar_inventory(callback: CallbackQuery):
    await send_file(
        callback=callback,
        filename="Барный инвентарь.pdf",
        caption="Вот документ для изучения Барный инвентарь",
    )


@router.callback_query(F.data == "syrups_toppings")
async def syrups_toppings(callback: CallbackQuery):
    await send_file(
        callback=callback,
        filename="Сиропы, топинги, пюре.pdf",
        caption="Вот документ для изучения Сиропы, топинги, пюре",
    )


@router.callback_query(F.data == "equipment")
async def syrups_toppings(callback: CallbackQuery):
    await delete_message(callback.message)
    await callback.message.answer(WAIT_FOR_TEXT)
