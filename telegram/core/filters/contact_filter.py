from aiogram.filters import BaseFilter
from aiogram.types import Message

class UserSendContact(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.contact and message.contact.user_id:
            return True
