from aiogram import Router, Bot, F
from aiogram.types import Message

from telegram.core.filters.chat_types_filter import ChatTypesFilter
from utils_custom.dir_utils import create_dir_if_not_exists
from utils_custom.file_utils import (basename_in_full_filename,
                                     compose_full_filename)



router_image_private = Router()
router_image_private.message.filter(ChatTypesFilter(["private"]))

@router_image_private.message(F.photo)
async def get_image_handler(message: Message, bot: Bot):
    file = await bot.get_file(file_id=message.photo[0].file_id)
    server_full_filename = file.file_path

    await message.answer(text=f"You have been sent an image "
                              f"file: '{server_full_filename}'")

    base_file_name = basename_in_full_filename(server_full_filename)

    local_full_file_name = compose_full_filename(
        path_directories=("telegram", "local_images_received"),
        file_name=base_file_name)

    create_dir_if_not_exists(local_full_file_name)

    await bot.download_file(file_path=server_full_filename,
                            destination=local_full_file_name)
