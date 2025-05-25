# bot/handlers.py

from pyrogram import Client, filters
from pyrogram.types import Message
from bot.shortlink import generate_shortlink
from bot.database import save_file, get_user_files
from bot.utils import log_to_channel
from bot.scheduler import schedule_deletion
from datetime import datetime

def register_handlers(app: Client):

    @app.on_message(filters.command("start"))
    async def start_handler(client, message: Message):
        await message.reply("Hey! Send me a file or use /link or /batch.")

    @app.on_message(filters.command("link"))
    async def link_handler(client, message: Message):
        if not message.reply_to_message:
            return await message.reply("Reply to a file, video, or text with `/link`.", quote=True)

        file = message.reply_to_message
        saved_msg = await save_file(client, file)

        shortlink = await generate_shortlink(saved_msg.link)
        await message.reply(f"Here is your link:\n`{shortlink}`", quote=True)

        await schedule_deletion(client, saved_msg.chat.id, saved_msg.id, message.from_user.id)
        await log_to_channel(client, f"#NEW_LINK by {message.from_user.id}")

    @app.on_message(filters.command("batch"))
    async def batch_handler(client, message: Message):
        if not message.reply_to_message:
            return await message.reply("Reply to a file in a batch with `/batch`.")

        batch_files = await get_user_files(message.from_user.id, limit=200)
        if not batch_files:
            return await message.reply("No files found.")

        batch_links = "\n".join([f"- {file['shortlink']}" for file in batch_files])
        await message.reply(f"Your batch:\n{batch_links}")
