from pyrogram import filters
from pyrogram.types import Message
from bot.filters import admin_filter
from bot.database import save_batch
from bot.utils import generate_short_id

def batch_handler(app):
    @app.on_message(filters.command("batch") & admin_filter)
    async def batch_cmd(client, message: Message):
        args = message.text.split()
        if len(args) != 3:
            return await message.reply("Usage: /batch <start_msg_id> <end_msg_id>")

        try:
            start_msg_id = int(args[1])
            end_msg_id = int(args[2])
        except ValueError:
            return await message.reply("Both IDs must be integers.")

        short_id = generate_short_id()
        save_batch(start_msg_id, end_msg_id, short_id, message.from_user.id)

        await message.reply(f"Batch link:\n`https://t.me/{client.me.username}?start={short_id}`")
