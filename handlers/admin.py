from pyrogram import filters
from pyrogram.types import Message
from bot.filters import admin_filter
from bot.config import ADMINS

def admin_handlers(app):
    @app.on_message(filters.command("admins") & admin_filter)
    async def list_admins(client, message: Message):
        text = "**Bot Admins:**\n"
        text += "\n".join(str(uid) for uid in ADMINS)
        await message.reply(text)
