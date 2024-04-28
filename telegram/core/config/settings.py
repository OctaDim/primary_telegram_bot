import os
from pathlib import Path
from dotenv import dotenv_values
from dataclasses import dataclass


@dataclass
class TelegramSettings:
    bot_name: str
    user_name: str
    user_id: str
    bot_token: str

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
FULL_ENV_FILENAME = os.path.join(BASE_DIR, ".env")

project_env_vars_dict = dotenv_values(FULL_ENV_FILENAME)

BOT_CREDENTIALS = TelegramSettings(
    bot_name=project_env_vars_dict.get("TELEGRAM_BOT_NAME"),
    user_name=project_env_vars_dict.get("TELEGRAM_USER_NAME"),
    user_id=project_env_vars_dict.get("TELEGRAM_USER_ID"),
    bot_token=project_env_vars_dict.get("TELEGRAM_BOT_TOKEN"))


RESTRICTED_WORDS = {"fuck", "shit", "fucker", "asshole"}
MAX_BOT_MSG_LENGTH = 4096
BAN_DURATION = 35








# @dataclass
# class Bots:
#     bot_token: str
#     user_id: int
#
# @dataclass
# class Settings:
#     bots: Bots
#
# def get_settings() -> Settings:
#     BASE_DIR = Path(__file__).resolve().parent.parent.parent
#     FULL_ENV_FILENAME = os.path.join(BASE_DIR, ".env")
#
#     project_env_vars_dict = dotenv_values(FULL_ENV_FILENAME)
#
#     TELEGRAM_BOT_TOKEN = project_env_vars_dict.get("TELEGRAM_BOT_TOKEN")
#     TELEGRAM_USER_ID = project_env_vars_dict.get("TELEGRAM_USER_ID")
#
#     bots = Bots(bot_token=TELEGRAM_BOT_TOKEN,
#                 user_id=int(TELEGRAM_USER_ID))
#
#     return Settings(bots=bots)
#
# SETTINGS = get_settings()
