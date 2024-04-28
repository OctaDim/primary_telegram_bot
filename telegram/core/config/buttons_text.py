from dataclasses import dataclass



@dataclass
class CommonButtonsText():
    START = "Start"
    MENU = "Ⓜ️ Main Menu"
    SAY_BYE = "🚪 Bye-Bye"


@dataclass
class OnStartKbdButtonsText(CommonButtonsText):
    FREE_TIME = "Free Time"
    ENROLL = "Enroll"
    PAYMENT = "Payment"
    PRICES = "Prices"
    ADMIN_CHAT = "Admin Chat"
    PORTFOLIO = "Portfolio"
    CONTACTS = "Contacts"
    # SAY_BYE = inherited from CommonButtonsText, redefine text and make handler if necessary
    ICONS = "Icons"
    ALL_ICONS = "All Icons"
    SEND_MY_CONTACT = "Send My Contact"
    MORE_ACTIONS = "More Actions >>"

@dataclass
class MoreActionsKbdButtonsText(CommonButtonsText):
    # MENU = inherited from 'CommonButtonsText', redefine text and make handler if necessary
    SEND_PHONE = "☎️ Send My Phone"
    SEND_LOCATION = "🌍 Send My Location"
    SEND_POLL = "📊 Send Poll"
    SEND_QUIZ = "❓ Send Quiz"
    SEND_REGULAR_POLL = "📋 Send Regular Poll"
    # SAY_BYE = inherited from 'CommonButtonsText', redefine text and make handler if necessary
