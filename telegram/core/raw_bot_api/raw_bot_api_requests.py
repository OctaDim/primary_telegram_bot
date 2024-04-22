import asyncio
import aiohttp  # pip install aiohttp
from telegram.core.config.settings import BOT_CREDENTIALS

TOKEN = BOT_CREDENTIALS.bot_token
BASE_URL = f"https://api.telegram.org/bot{TOKEN}/"


async def send_message(chat_id, text):
    async with aiohttp.ClientSession() as session:
        params = {"chat_id": chat_id, "text": text}
        url = BASE_URL + "sendMessage"
        async with session.post(url=url, data=params) as response:
            await response.json()


async def handle_updates(new_update_dict: dict):
    message = new_update_dict.get("message", False)
    if message:
        chat_id = message.get("chat").get("id")
        # chat_id = message['chat']['id']
        text = message.get("text", False)
        if text:
            await send_message(chat_id, f"Echo: {text}")
        else:
            await send_message(chat_id, "Only text can be handled")


async def get_updates():
    offset = None
    async with aiohttp.ClientSession() as session:
        while True:
            params = {'timeout': 10, 'offset': offset}
            url = BASE_URL + "getUpdates"

            async with session.post(url=url, data=params) as response:
                updates = await response.json()
                new_updates_dicts_list = updates.get("result")

                if new_updates_dicts_list:
                    offset = new_updates_dicts_list[-1].get("update_id") + 1

                    for each_new_update_dict in new_updates_dicts_list:
                        await handle_updates(each_new_update_dict)
                        print(each_new_update_dict)
                        print(offset)


async def main():
    await get_updates()


asyncio.run(main())
