# main.py

import os
import asyncio
from pyrogram import Client
from dotenv import load_dotenv

from bot.handlers import register_handlers
from bot.utils import log_to_channel

load_dotenv("config.env")

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
LOGS_CHANNEL_ID = int(os.getenv("LOGS_CHANNEL_ID"))

app = Client("file_share_bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

async def main():
    await app.start()
    await log_to_channel(app, "Lakki, I am back!")
    register_handlers(app)
    await app.idle()

if __name__ == "__main__":
    asyncio.run(main())
