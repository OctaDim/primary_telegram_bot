from aiogram.filters import Filter, BaseFilter
from aiogram.types import Message



class ChatTypesFilter(Filter):
    def __init__(self, chat_types: list[str]):
        self.chat_types = chat_types

    async def __call__(self, message: Message, *args, **kwargs) -> bool:
        chat_type_matches = message.chat.type in self.chat_types
        return chat_type_matches


class IsPrivateChatFilter(Filter):
    async def __call__(self, message: Message, *args, **kwargs) -> bool:
        chat_is_private = (message.chat.type == "private")
        return chat_is_private


class IsGroupChatFilter(Filter):
    async def __call__(self, message: Message, *args, **kwargs) -> bool:
        chat_is_group = (message.chat.type == "group")
        return chat_is_group


class IsSuperGroupFilter(Filter):
    async def __call__(self, message: Message, *args, **kwargs) -> bool:
        chat_is_supergroup = (message.chat.type == "supergroup")
        return chat_is_supergroup
