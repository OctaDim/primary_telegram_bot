from aiogram.types import (KeyboardButtonPollType,
                           ReplyKeyboardRemove,
                           ReplyKeyboardMarkup,
                           KeyboardButton)

from aiogram.utils.keyboard import ReplyKeyboardBuilder

from telegram.core.config.buttons_text import  MoreActionsKbdButtonsText



def get_more_actions_keyboard():
    builder = ReplyKeyboardBuilder()

    builder.button(text=MoreActionsKbdButtonsText.SEND_PHONE,
                   request_contact=True)

    builder.button(text=MoreActionsKbdButtonsText.SEND_LOCATION,
                   request_location=True)

    builder.button(text=MoreActionsKbdButtonsText.SEND_POLL,
                   request_poll=KeyboardButtonPollType())

    builder.button(text=MoreActionsKbdButtonsText.SEND_QUIZ,
                   request_poll=KeyboardButtonPollType(type="quiz"))

    builder.button(text=MoreActionsKbdButtonsText.SEND_REGULAR_POLL,
                   request_poll=KeyboardButtonPollType(type="regular"))

    builder.button(text=MoreActionsKbdButtonsText.MENU)

    builder.button(text=MoreActionsKbdButtonsText.SAY_BYE)

    builder.adjust(2, 3, 2)
    connect_keyboard_markup = builder.as_markup(
        input_field_placeholder="Select actions:",
        resize_keyboard=True,
        one_time_keyboard=True)

    return connect_keyboard_markup
