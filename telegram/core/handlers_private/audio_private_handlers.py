from aiogram import Router, F
from aiogram.types import Message

from telegram.core.filters.chat_types_filter import ChatTypesFilter



router_audio_private = Router()
router_audio_private.message.filter(ChatTypesFilter(["private"]))


@router_audio_private.message(F.audio)
async def text_messages_handler(message: Message):
    await message.answer(text=f"Audio message have been received")
