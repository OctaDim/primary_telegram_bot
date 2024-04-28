from aiogram import Router, Bot
from aiogram.types import Message

from telegram.core.config.settings import BOT_CREDENTIALS
from telegram.core.filters.chat_types_filter import ChatTypesFilter



router_echo_private = Router()
router_echo_private.message.filter(ChatTypesFilter(["private"]))

@router_echo_private.message()
async def echo_handler(message: Message, bot: Bot):
    if message.poll:
        await message.forward(chat_id=message.chat.id)
        return
    # if message.sticker:
    #     await message.bot.send_chat_action(chat_id=message.chat.id,
    #
    try:
        await message.answer(text="This is an echo message of your message:")
        await message.send_copy(BOT_CREDENTIALS.user_id)

        # await message.reply(text="Reply")

    except TypeError:
        await message.answer("It isn't possible to return "
                             "a copy of this message.")  # Not all the types is supported to be copied so need to handle it
