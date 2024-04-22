from aiogram import Router, Bot, F
from aiogram.filters import Command
from aiogram.filters.logic import or_f
from aiogram.types import Message



router_text_msg_private = Router()

@router_text_msg_private.message(F.text == "Hallo")
async def text_messages_handler(message: Message):
    await message.answer(text=f"Hallo, {message.from_user.full_name}! (1)")


@router_text_msg_private.message(Command("greetings"))
@router_text_msg_private.message(F.text.lower().startswith(("hallo", "hi")))
# @router_text_msg_private.message(F.text.startswith("hallo")|(F.text.startswith("hello")|(F.textstartswith("hi"))
async def text_messages_handler(message: Message):
    await message.answer(text=f"Hallo2, {message.from_user.full_name}! (2)")


@router_text_msg_private.message(
    or_f(Command("shipment"), F.text.lower().startswith(("ship", "load"))))
async def text_messages_handler(message: Message):
    await message.answer(text=f"Command '{message.text}' (or_f)")
