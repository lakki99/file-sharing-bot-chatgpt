from pyrogram import filters
from pyrogram.types import Message
from bot.filters import admin_filter
from bot.database import save_file
from bot.utils import generate_short_id, get_expiry_timestamp

def link_handler(app):
    @app.on_message(filters.command("link") & admin_filter)
    async def link_cmd(client, message: Message):
        if not message.reply_to_message or not message.reply_to_message.media:
            return await message.reply("Reply to a media message to generate link.")

        file_msg = message.reply_to_message
        file_id = file_msg.id
        short_id = generate_short_id()
        expiry_ts = get_expiry_timestamp()

        save_file(file_id, short_id, expiry_ts, message.from_user.id)
        await message.reply(f"Link generated:\n`https://t.me/{client.me.username}?start={short_id}`")
