import asyncio

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats

from core.commands import Commands
from core.config import settings
from core.log import configure_logging
from routers import router


async def main() -> None:
    """
    Функция для запуска бота

    :return: None
    """
    configure_logging()

    dp = Dispatcher()

    dp.include_router(router)
    commands = [
        BotCommand(command=command.name, description=command) for command in Commands
    ]
    bot = Bot(
        token=settings.bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    await bot.set_my_commands(commands, BotCommandScopeAllPrivateChats())
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
