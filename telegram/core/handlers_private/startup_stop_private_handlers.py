from datetime import datetime
from aiogram import Router, Bot
from telegram.core.config.settings import BOT_CREDENTIALS



router_start_stop_bot_private = Router()

@router_start_stop_bot_private.startup()
async def startup_bot_handler(bot: Bot, **kwargs):
    await bot.send_message(
        chat_id=BOT_CREDENTIALS.user_id,
        text=f"Telegram bot started [{kwargs.get("bot_started")}]")


@router_start_stop_bot_private.shutdown()
async def shutdown_bot_handler(bot: Bot):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M")

    await bot.send_message(
        chat_id=BOT_CREDENTIALS.user_id,
        text=f"Telegram bot shutdown [{current_datetime}]")
