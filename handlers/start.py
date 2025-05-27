from pyrogram import filters
from pyrogram.types import Message

def start_handlers(app):
    @app.on_message(filters.command("start") & filters.private)
    async def start(client, message: Message):
        print(f"[DEBUG] Received /start from {message.from_user.id}")  # Debug print
        await message.reply("Hi! Welcome to the File Sharing Bot.")
