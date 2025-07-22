from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.inline.c1 import c1_options
from utils.files import send_file
from utils.tg import edit_message_or_write_new


router = Router(name=__name__)


@router.callback_query(F.data == "1с")
async def get_options(callback: CallbackQuery):
    await edit_message_or_write_new(
        message=callback.message, text="Выберите подкатегорию", markup=c1_options()
    )


@router.callback_query(F.data == "create_order")
async def create_order(callback: CallbackQuery):
    await send_file(
        callback=callback,
        filename="Создание_Заказа_Покупателя_и_выставление_счёта.pdf",
        caption="Вот документ для изучения Создание Заказа Покупателя и выставление счёта.",
    )


@router.callback_query(F.data == "create_shipment")
async def create_shipment(callback: CallbackQuery):
    await send_file(
        callback=callback,
        filename="Создание отгрузочной накладной.pdf",
        caption="Вот документ для изучения Создание отгрузочной накладной",
    )


@router.callback_query(F.data == "customer_return")
async def customer_return(callback: CallbackQuery):
    await send_file(
        callback=callback,
        filename="Возврат от покупателя.pdf",
        caption="Вот документ для изучения Возврат от покупателя",
    )


@router.callback_query(F.data == "create_counterparty")
async def create_counterparty(callback: CallbackQuery):
    await send_file(
        callback=callback,
        filename="Создание контрагента.pdf",
        caption="Вот документ для изучения Создание контрагента",
    )


@router.callback_query(F.data == "create_nomenclature")
async def create_nomenclature(callback: CallbackQuery):
    await send_file(
        callback=callback,
        filename="Создание номенклатуры.pdf",
        caption="Вот документ для изучения Создание номенклатуры",
    )
