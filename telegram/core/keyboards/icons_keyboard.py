from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from telegram.core.config.buttons_icons import BUTTON_ICONS



def get_icons_keyboard() -> ReplyKeyboardMarkup:
    icons_buttons_list = [KeyboardButton(text=icon) for icon in BUTTON_ICONS]

    icons_keyboard_markup = ReplyKeyboardMarkup(
        keyboard=[icons_buttons_list],
        resize_keyboard=True)

    return icons_keyboard_markup
