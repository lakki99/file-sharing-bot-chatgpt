# bot/utils.py

import os
from pyrogram import Client
from pyrogram.types import Message

from dotenv import load_dotenv
load_dotenv("config.env")

LOGS_CHANNEL_ID = int(os.getenv("LOGS_CHANNEL_ID"))

async def log_to_channel(client: Client, text: str):
    try:
        await client.send_message(chat_id=LOGS_CHANNEL_ID, text=text)
    except Exception as e:
        print(f"Logging failed: {e}")
