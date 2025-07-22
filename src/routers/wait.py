from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.inline.builder import generate_inline_kb
from keyboards.inline.common import get_common_buttons
from utils.tg import edit_message_or_write_new

router = Router(name=__name__)


@router.callback_query(
    F.data.in_(
        (
            "service",
            "company",
            "support",
        )
    )
)
async def to_back(callback: CallbackQuery):
    await edit_message_or_write_new(
        message=callback.message,
        text="Выберите подкатегорию",
        markup=generate_inline_kb(data_with_buttons=get_common_buttons()),
    )
