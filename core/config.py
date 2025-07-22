from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class BotSettings(BaseSettings):
    token: str
    model_config = SettingsConfigDict(case_sensitive=False, env_prefix="bot_")


class Settings(BaseSettings):
    """
    Настройки приложения
    """

    bot: BotSettings = BotSettings()
    model_config = SettingsConfigDict(
        case_sensitive=False,
    )


settings = Settings()
