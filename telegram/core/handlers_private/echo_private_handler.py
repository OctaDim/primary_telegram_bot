from aiogram import Router, Bot
from aiogram.types import Message
from telegram.core.config.settings import BOT_CREDENTIALS



router_echo_private = Router()

@router_echo_private.message()
async def echo_handler(message: Message, bot: Bot):
    try:
        await bot.send_message(chat_id=message.from_user.id,
                               text="Echo handler result:")
        await message.send_copy(BOT_CREDENTIALS.user_id)
        await message.answer(text="Answer")
        await message.reply(text="Reply")

    except TypeError:
        await message.answer("It isn't possible to return "
                             "a copy of this message.")  # Not all the types is supported to be copied so need to handle it
