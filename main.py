from pyrogram import Client
from bot.config import API_ID, API_HASH, BOT_TOKEN
from bot.cleanup import start_cleanup_job
from handlers import register_handlers

app = Client(
    "file_share_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message()
async def log_all(_, message):
    print(f"[LOG] {message.from_user.id}: {message.text}")

if __name__ == "__main__":
    register_handlers(app)
    start_cleanup_job()
    print("Bot started...")
    app.run()
