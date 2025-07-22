from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from core.commands import Commands
from keyboards.inline.menu import menu_kb, MENU_CB
from utils.tg import delete_message

router = Router(name=__name__)

TEXT = "Здравствуйте, что бы вы хотели узнать?"


@router.message(Command(Commands.start.name))
async def handle_help_by_command(message: Message):
    await message.answer(TEXT, reply_markup=menu_kb())


@router.callback_query(F.data == MENU_CB)
async def handle_help_by_callback(callback: CallbackQuery):
    await delete_message(callback.message)
    await callback.message.answer(TEXT, reply_markup=menu_kb())
