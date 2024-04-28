import logging
import asyncio
from datetime import datetime

from aiogram import Dispatcher, Bot, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from telegram.core.config.settings import BOT_CREDENTIALS
from telegram.core.config.commands_text import CommandsText

from telegram.core.handlers_group.text_group_handlers import router_text_msg_group

from telegram.core.handlers_private.startup_stop_private_handlers import router_start_stop_bot_private
from telegram.core.handlers_private.commands_private_handlers import  router_commands_private
from telegram.core.handlers_private.text_private_handlers import  router_text_msg_private
from telegram.core.handlers_private.image_private_handlers import  router_image_private
from telegram.core.handlers_private.audio_private_handlers import  router_audio_private
from telegram.core.handlers_private.echo_private_handler import router_echo_private



logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(name)s - "
                           "(%(filename)s).%(funcName)s(%(lineno)d) - "
                           "%(message)s")


dp = Dispatcher(storage=MemoryStorage())
dp["bot_started"] = datetime.now().strftime("%Y-%m-%d %H:%M")


dp.include_routers(
    router_text_msg_group,

    router_start_stop_bot_private,
    router_commands_private,
    router_text_msg_private,
    router_image_private,
    router_audio_private,
    router_echo_private,
    )


# ALLOWED_UPDATES = ["message", "edited_message"]

private_chat_bot_commands_list = [
    types.BotCommand(command=CommandsText.START, description="Command '/start'"),
    types.BotCommand(command=CommandsText.MORE_ACTIONS, description="Menu 'More Actions'"),
    types.BotCommand(command=CommandsText.QUIT, description="Close main menu"),
]

group_chat_bot_commands_list = [
    types.BotCommand(command=CommandsText.START, description="Command '/start'"),
    types.BotCommand(command=CommandsText.MORE_ACTIONS, description="Menu 'More Actions'"),
    types.BotCommand(command=CommandsText.QUIT, description="Close main menu"),
]


async def main() -> None:

    bot = Bot(token=BOT_CREDENTIALS.bot_token,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await bot.delete_webhook(drop_pending_updates=True)

    await bot.set_my_commands(commands=[*group_chat_bot_commands_list],
                              scope=types.BotCommandScopeAllGroupChats())

    await bot.set_my_commands(commands=[*private_chat_bot_commands_list],
                              scope=types.BotCommandScopeAllPrivateChats())
    # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())



    try:
        await dp.start_polling(bot,
                               allowed_updates=dp.resolve_used_update_types())
        # await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
