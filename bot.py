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
    # Optional: you can register default start handler here if needed
    pass

async def startup():
    await log_to_channel(app, "Lakki, I am back!")
    register_handlers(app)

app.startup = startup  # if using pyrogram 2.x or add in start manually

if __name__ == "__main__":
    register_handlers(app)
    app.run()
