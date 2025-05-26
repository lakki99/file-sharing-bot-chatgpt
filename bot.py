from pyrogram import Client
from bot.handlers import register_handlers
from bot.config import API_ID, API_HASH, BOT_TOKEN

app = Client("file_sharing_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

register_handlers(app)

app.run()