from pyrogram import Client
from bot.config import API_ID, API_HASH, BOT_TOKEN
from handlers import register_handlers
from bot.cleanup import start_cleanup_job

app = Client("file_share_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Register all command handlers
register_handlers(app)

# Start background cleanup job
start_cleanup_job()

# Run the bot
app.run()