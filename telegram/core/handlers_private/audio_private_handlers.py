from aiogram import Router, Bot, F
from aiogram.types import Message

from telegram.core.config.settings import BOT_CREDENTIALS



router_audio_private = Router()

@router_audio_private.message(F.audio)
async def text_messages_handler(message: Message):
    await message.answer(text=f"Audio message have been received")
