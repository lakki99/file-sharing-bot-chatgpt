import os
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

@app.on_message()
async def on_start_message(client, message):
    pass  # optional message handler

@app.on_start()
async def startup(client):
    await log_to_channel(client, "Lakki, I am back!")
    await register_handlers(client)

if __name__ == "__main__":
    app.run()
