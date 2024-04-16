import json
from aiogram import Bot
from aiogram.types import Message

from telegram.core.config.settings import (TELEGRAM_BOT_CREDENTIALS,
                                           MAX_BOT_MSG_LENGTH)

from utils_custom.file_utils import (get_file_basename_from_full_filename,
                                     compose_full_filename)

from utils_custom.dir_utils import create_dir_if_not_exists



async def start_bot_handler(bot: Bot):
    await bot.send_message(TELEGRAM_BOT_CREDENTIALS.user_id,
                           text="Telegram Bot started")


async def stop_bot_handler(bot: Bot):
    await bot.send_message(TELEGRAM_BOT_CREDENTIALS.user_id,
                           text="Telegram Bot stopped")


async def get_start_run_go_commands_handler(message: Message, bot: Bot):
    await bot.send_message(
        TELEGRAM_BOT_CREDENTIALS.user_id,
        text=f"Message from <b>{message.from_user.username}</b> received")

    await message.answer(
        text=f"Message from <u>{message.from_user.full_name}</u> received")

    await message.reply(
        text=f"Message from <tg-spoiler>{message.from_user.id}</tg-spoiler>"
             f" received and replied")


async def get_photo_handler(message: Message, bot: Bot):
    file = await bot.get_file(file_id=message.photo[-1].file_id)
    server_full_filename = file.file_path

    await message.answer(
        text=f"You have been sent an image file: '{server_full_filename}'")

    base_file_name = get_file_basename_from_full_filename(server_full_filename)

    local_full_file_name = compose_full_filename(
        directories_paths=("telegram", "images_received"), file_name=base_file_name)

    create_dir_if_not_exists(local_full_file_name)

    await bot.download_file(file_path=server_full_filename,
                            destination=local_full_file_name)


async def get_message_echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("It isn't possible to return a copy of this message.")  # Not all the types is supported to be copied so need to handle it


async def get_hallo_message(message: Message):
    await message.answer(text=f"Hallo, {message.from_user.full_name}!")


async def get_json_message(message: Message, bot: Bot):
    json_str = json.dumps(message.model_dump(), indent=4, default=str)

    for start_point in range(0, len(json_str), MAX_BOT_MSG_LENGTH):
        msg_part = json_str[start_point: start_point + MAX_BOT_MSG_LENGTH]
        await bot.send_message(text=f"```{message.chat.id, msg_part}```")
