from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from telegram.core.config.buttons_text import OnStartKbdButtonsText



def get_on_start_keyboard() -> ReplyKeyboardMarkup:
    free_time_btn = KeyboardButton(text=OnStartKbdButtonsText.FREE_TIME)
    enroll_btn = KeyboardButton(text=OnStartKbdButtonsText.ENROLL)
    payment_btn = KeyboardButton(text=OnStartKbdButtonsText.PAYMENT)
    prices_btn = KeyboardButton(text=OnStartKbdButtonsText.PRICES)
    admin_chat_btn = KeyboardButton(text=OnStartKbdButtonsText.ADMIN_CHAT)
    portfolio_btn = KeyboardButton(text=OnStartKbdButtonsText.PORTFOLIO)
    contacts_btn = KeyboardButton(text=OnStartKbdButtonsText.CONTACTS)
    bye_btn = KeyboardButton(text=OnStartKbdButtonsText.SAY_BYE)
    icons_btn = KeyboardButton(text=OnStartKbdButtonsText.ICONS)
    all_icons_btn = KeyboardButton(text=OnStartKbdButtonsText.ALL_ICONS)
    more_actions_btn = KeyboardButton(text=OnStartKbdButtonsText.MORE_ACTIONS)

    start_keyboard_markup = ReplyKeyboardMarkup(
        keyboard=[[free_time_btn, enroll_btn],
                  [portfolio_btn, prices_btn, payment_btn],
                  [admin_chat_btn, contacts_btn],
                  [more_actions_btn, bye_btn],
                  [icons_btn, all_icons_btn]],
        resize_keyboard=True,
        # one_time_keyboard=True,
    )

    return start_keyboard_markup
