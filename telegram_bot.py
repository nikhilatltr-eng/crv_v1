from telegram import Bot
import asyncio

TOKEN = "8041345304:AAHZnOMdDdwIZTavl5HI6x-8Xuu8kwQaj9I"
CHAT_ID = "7366145742"


async def send_message(text):

    bot = Bot(token=TOKEN)

    await bot.send_message(
        chat_id=CHAT_ID,
        text=text
    )


async def main():

    await send_message(
        "crv_v1 TEST MESSAGE"
    )


asyncio.run(main())