import time

from aiogram import Router, Bot, F
from aiogram.filters import or_f
from aiogram.types import Message


from telegram.core.filters.chat_types_filter import ChatTypesFilter
from utils_custom.text_utils import clean_text_punctuation

from telegram.core.config.settings import (RESTRICTED_WORDS,
                                           BAN_DURATION)

from telegram.core.filters.chat_types_filter import (IsPrivateChatFilter,
                                                     IsGroupChatFilter,
                                                     IsSuperGroupFilter)



router_text_msg_group = Router()
router_text_msg_group.message.filter(ChatTypesFilter(["group", "supergroup"]))


@router_text_msg_group.edited_message()
@router_text_msg_group.message()
async def text_messages_handler(message: Message):
    cleaned_msg = clean_text_punctuation(message.text)
    cleaned_words_set = cleaned_msg.lower().split()
    bad_words_intersection = RESTRICTED_WORDS.intersection(cleaned_words_set)

    if bad_words_intersection:
        username = message.from_user.username
        await message.delete()
        await message.answer(text=f"Using abuse words are not allowed in common group! "
                                  f"\nMessage from [{username}] was removed")

        # if BAN_DURATION > 30:
        #     await message.chat.ban(user_id=message.from_user.id,
        #                            until_date=int(time.time()+BAN_DURATION))
        #     await message.answer(text=f"User '{username}' is banned "
        #                               f"for {BAN_DURATION} seconds")
