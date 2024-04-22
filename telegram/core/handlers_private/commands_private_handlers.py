from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command, CommandStart



router_commands_private = Router()

@router_commands_private.message(CommandStart())
async def start_command_handler(message: Message):
    await message.answer(f"Command {message.text} have been typed")


@router_commands_private.message(Command("menu"))
async def menu_command_handler(message: Message):
    await message.answer(f"Command {message.text} have been typed")


@router_commands_private.message(Command("free_time"))
async def menu_command_handler(message: Message):
    await message.answer(f"Command {message.text} have been typed")


@router_commands_private.message(Command("enrol"))
async def menu_command_handler(message: Message):
    await message.answer(f"Command {message.text} have been typed")


@router_commands_private.message(Command("payment"))
async def menu_command_handler(message: Message):
    await message.answer(f"Command {message.text} have been typed")


@router_commands_private.message(Command("admin_chat"))
async def menu_command_handler(message: Message):
    await message.answer(f"Command {message.text} have been typed")


@router_commands_private.message(Command("portfolio"))
async def menu_command_handler(message: Message):
    await message.answer(f"Command {message.text} have been typed")


@router_commands_private.message(Command("prices"))
async def menu_command_handler(message: Message):
    await message.answer(f"Command {message.text} have been typed")


@router_commands_private.message(Command("contacts"))
async def menu_command_handler(message: Message):
    await message.answer("Command '/contacts' have been typed")
