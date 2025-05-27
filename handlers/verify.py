from pyrogram import filters
from pyrogram.types import Message
from bot.filters import admin_filter
from bot.database import verify_user

def verify_handler(app):
    @app.on_message(filters.command("verify") & admin_filter)
    async def verify_cmd(client, message: Message):
        if len(message.command) < 2:
            return await message.reply("Usage: /verify <user_id>")

        try:
            user_id = int(message.command[1])
            verify_user(user_id)
            await message.reply(f"User {user_id} verified successfully.")
        except ValueError:
            await message.reply("Invalid user_id.")
