from datetime import datetime

from aiogram import Router, Bot

from telegram.core.config.settings import BOT_CREDENTIALS
from telegram.core.filters.chat_types_filter import ChatTypesFilter



router_start_stop_bot_private = Router()
router_start_stop_bot_private.message.filter(
    ChatTypesFilter(["private", "group", "supergroup"]))


@router_start_stop_bot_private.startup()
async def startup_bot_handler(bot: Bot, **kwargs):
    await bot.send_message(chat_id=BOT_CREDENTIALS.user_id,
        text=f"[{kwargs.get("bot_started")}] Telegram bot started")


@router_start_stop_bot_private.shutdown()
async def shutdown_bot_handler(bot: Bot, **kwargs):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M")
    await bot.send_message(
        chat_id=BOT_CREDENTIALS.user_id,
        text=f"[{current_datetime}] Telegram bot shutdown")
