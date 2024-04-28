from aiogram import Router, F
from aiogram.filters import Command
from aiogram.filters.logic import or_f, and_f
from aiogram.types import Message
from aiogram.types import ReplyKeyboardRemove

from telegram.core.filters.chat_types_filter import ChatTypesFilter
from telegram.core.filters.contact_filter import UserSendContact

from telegram.core.keyboards.on_start_keyboard import get_on_start_keyboard
from telegram.core.keyboards.icons_keyboard import  get_icons_keyboard
from telegram.core.keyboards.icons_keyboard_builder import get_icons_keyboard_builder
from telegram.core.keyboards.more_actions_keyboard import get_more_actions_keyboard


from telegram.core.config.buttons_text import (CommonButtonsText,
                                               OnStartKbdButtonsText,
                                               MoreActionsKbdButtonsText)



router_text_msg_private = Router()
router_text_msg_private.message.filter(ChatTypesFilter(["private"]))


@router_text_msg_private.message(
    lambda F: F.text == CommonButtonsText.START
              or F.text == OnStartKbdButtonsText.MENU)
async def text_messages_handler(message: Message):
    await message.answer(text=f"Okay, {message.from_user.first_name}."
                              f"\nYou have typed '{message.text}'."
                              f"\nHere is main menu:",
                         reply_markup=get_on_start_keyboard())


@router_text_msg_private.message(Command("greetings"))
@router_text_msg_private.message(F.text.lower().startswith(("hallo", "hi")))
# @router_text_msg_private.message(F.text.startswith("hallo")|(F.text.startswith("hello")|(F.textstartswith("hi"))
async def text_messages_handler(message: Message):
    await message.answer(text=f"Hallo, {message.from_user.full_name}!"
                              f"\nLets start with main menu:",
                         reply_markup=get_on_start_keyboard())


@router_text_msg_private.message(F.text == OnStartKbdButtonsText.SAY_BYE)
async def text_messages_handler(message: Message):
    await message.answer(text=f"You have typed '{message.text}'."
                              f"\nSo, bye-bye!"
                              f"\nYou can /start again any time.",
                         reply_markup=ReplyKeyboardRemove())


@router_text_msg_private.message(F.text == OnStartKbdButtonsText.ICONS)
async def text_messages_handler(message: Message):
    await message.answer(text=f"You have typed '{message.text}'."
                              f"\nNOTE: Only 8 symbols can be displayed "
                              f"(words even less)",
                         reply_markup=get_icons_keyboard())


@router_text_msg_private.message(F.text == OnStartKbdButtonsText.ALL_ICONS)
async def text_messages_handler(message: Message):
    await message.answer(text=f"You have typed '{message.text}'."
                              f"\nAll icons are displayed through Builder",
                         reply_markup=get_icons_keyboard_builder())


@router_text_msg_private.message(F.text == OnStartKbdButtonsText.MORE_ACTIONS)
async def text_messages_handler(message: Message):
    await message.answer(text=f"You have typed '{message.text}'."
                              f"\nOK, select action, you want.",
                         reply_markup=get_more_actions_keyboard())


@router_text_msg_private.message(UserSendContact())
async def text_messages_handler(message: Message):
    if message.contact.user_id == message.from_user.id:
        contact_owner = "your own"
    else:
        contact_owner = "other person's"

    await message.answer(text=f"{message.from_user.first_name.upper()}, "
                          f"you have sent {contact_owner} contact "
                          f"'{message.contact.phone_number}'")


@router_text_msg_private.message(
    or_f(Command("shipment"), F.text.lower().startswith(("ship", "load"))))
async def text_messages_handler(message: Message):
    await message.answer(text=f"Command '{message.text}' (or_f)")


# ################ LAMBDA USAGE EXAMPLE ################################
# @router_text_msg_private.message(lambda message:
#     ("shipment" in message.text.lower())
#     or message.text.lower().startswith(("ship", "load")))
# async def text_messages_handler(message: Message):
#     await message.answer(text=f"You have typed '{message.text}' (lambda)")
