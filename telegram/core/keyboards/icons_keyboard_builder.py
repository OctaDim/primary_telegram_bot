from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from telegram.core.config.buttons_icons import BUTTON_ICONS



def get_icons_keyboard_builder() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    for icon in BUTTON_ICONS:
        builder.button(text=icon)
        # builder.add(KeyboardButton(text=icon))

    builder.adjust(3, 3, 1, 8)  # Example
    # builder.adjust(3)  # Example

    builder.row(KeyboardButton(text=BUTTON_ICONS[10]),  # Example: add new row
                KeyboardButton(text=BUTTON_ICONS[11]),
                KeyboardButton(text=BUTTON_ICONS[12]))

    builder.add(KeyboardButton(text=BUTTON_ICONS[1]),  # Example: add to the last row
                KeyboardButton(text=BUTTON_ICONS[2]),
                KeyboardButton(text=BUTTON_ICONS[3]))

    icons_keyboard_markup = builder.as_markup(resize_keyboard=True)
    return icons_keyboard_markup
