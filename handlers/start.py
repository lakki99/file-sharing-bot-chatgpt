from pyrogram import filters
from pyrogram.types import Message
from bot.database import add_user, is_admin, is_verified

def start_handler(app):
    @app.on_message(filters.command("start"))
    async def start_cmd(client, message: Message):
        user_id = message.from_user.id
        add_user(user_id)

        if is_admin(user_id):
            await message.reply_text("Welcome Admin! You have full access.")
        elif is_verified(user_id):
            await message.reply_text("You're verified! You can receive file links.")
        else:
            await message.reply_text("You're not verified yet. Please wait for admin approval.")
