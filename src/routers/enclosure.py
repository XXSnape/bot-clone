from aiogram import Router, F
from aiogram.types import CallbackQuery

from core.texts import WAIT_FOR_TEXT
from keyboards.inline.builder import generate_inline_kb
from keyboards.inline.common import get_common_buttons
from keyboards.inline.enclosure import enclosure_options, first_kb, sub_category_kb

from utils.tg import edit_message_or_write_new, delete_message

router = Router(name=__name__)


@router.callback_query(F.data == "enclosure")
async def get_options(callback: CallbackQuery):
    await edit_message_or_write_new(
        message=callback.message,
        text="Выберите подкатегорию",
        markup=enclosure_options(),
    )


@router.callback_query(F.data == "first")
async def first(callback: CallbackQuery):
    await edit_message_or_write_new(
        message=callback.message,
        text="Выберите подкатегорию",
        markup=first_kb(),
    )


@router.callback_query(F.data == "sub_category")
async def sub_category(callback: CallbackQuery):
    await edit_message_or_write_new(
        message=callback.message,
        text="Выберите подподкатегорию",
        markup=sub_category_kb(),
    )


@router.callback_query(F.data == "final")
async def final(callback: CallbackQuery):
    await edit_message_or_write_new(
        message=callback.message,
        text="Просто проверка, ничего важного",
        markup=generate_inline_kb(
            data_with_buttons=get_common_buttons(with_back=False)
        ),
    )


@router.callback_query(F.data == "third")
async def third(callback: CallbackQuery):
    await delete_message(callback.message)
    await callback.message.answer(WAIT_FOR_TEXT)
