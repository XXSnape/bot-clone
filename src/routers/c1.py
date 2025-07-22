from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.inline.c1 import c1_options
from utils.tg import edit_message_or_write_new, delete_message

router = Router(name=__name__)


@router.callback_query(F.data == "1с")
async def get_options(callback: CallbackQuery):
    await edit_message_or_write_new(
        message=callback.message, text="Выберите подкатегорию", markup=c1_options()
    )


@router.callback_query(F.data == "create_order")
async def create_order(callback: CallbackQuery):
    await delete_message(callback.message)
    file = FSInputFile
