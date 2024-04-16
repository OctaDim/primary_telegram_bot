import logging
import asyncio
import json
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import (Command,
                             CommandStart)

from telegram.core.config.settings import TELEGRAM_BOT_CREDENTIALS

from telegram.core.handlers.basic_handlers import (start_bot_handler,
                                                   stop_bot_handler,
                                                   get_message_echo_handler,
                                                   get_start_run_go_commands_handler,
                                                   get_photo_handler,
                                                   get_hallo_message,
                                                   get_json_message)



async def main() -> None:
    logging.basicConfig(level=logging.DEBUG,
                        # stream=sys.stdout,
                        format="%(asctime)s - %(levelname)s - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - "
                               "%(message)s")

    bot = Bot(token=TELEGRAM_BOT_CREDENTIALS.bot_token,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()

    dp.startup.register(start_bot_handler)
    dp.shutdown.register(stop_bot_handler)

    dp.message.register(get_start_run_go_commands_handler,
                        Command(commands=["start", "run", "go"]))

    dp.message.register(get_start_run_go_commands_handler, CommandStart())

    dp.message.register(get_hallo_message, F.text == "Hallo")

    dp.message.register(get_json_message,
                        Command(commands="json"))

    dp.message.register(get_photo_handler, F.photo)

    dp.message.register(get_message_echo_handler)





    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
