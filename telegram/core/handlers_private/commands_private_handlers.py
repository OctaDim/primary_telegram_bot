from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters.command import Command, CommandStart
from aiogram.types import ReplyKeyboardRemove

from telegram.core.filters.chat_types_filter import ChatTypesFilter
from telegram.core.config.commands_text import  CommandsText
from telegram.core.keyboards.on_start_keyboard import get_on_start_keyboard
from telegram.core.keyboards.more_actions_keyboard import  get_more_actions_keyboard




router_commands_private = Router()
router_commands_private.message.filter(ChatTypesFilter(["private"]))


@router_commands_private.message(CommandStart())
async def start_command_handler(message: Message):
    await message.answer(text=f"Command {message.text} have been typed."
                              f"\nHallo, I'm virtual assistant."
                              f"\nLets start with main menu first.",
                         reply_markup=get_on_start_keyboard())


@router_commands_private.message(Command(CommandsText.MENU))
async def menu_command_handler(message: Message):
    await message.answer(text=f"Command {message.text} have been typed"
                              f"\nHere is main menu, as you had ordered",
                         reply_markup=get_on_start_keyboard())


@router_commands_private.message(Command(CommandsText.MORE_ACTIONS))
async def menu_command_handler(message: Message):
    await message.answer(text=f"Command {message.text} have been typed"
                              f"\nHere is menu 'More Actions':",
                         reply_markup=get_more_actions_keyboard())


@router_commands_private.message(Command(CommandsText.QUIT))
async def menu_command_handler(message: Message):
    await message.answer(text=f"Command {message.text} have been typed "
                              f"\nOK. You can /start again any time.",
                         reply_markup=ReplyKeyboardRemove())
