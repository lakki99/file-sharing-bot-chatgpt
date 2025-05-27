from pyrogram import filters
from pyrogram.types import Message
from bot.filters import admin_filter
from bot.database import get_top_files, count_all_files

def stats_handler(app):
    @app.on_message(filters.command("stats") & admin_filter)
    async def stats_cmd(client, message: Message):
        top = get_top_files()
        total = count_all_files()

        if not top:
            return await message.reply("No files found.")

        text = f"**Top Used Links:**\n"
        for i, file in enumerate(top, 1):
            text += f"{i}. `{file['_id']}` - {file['clicks']} clicks\n"

        text += f"\n**Total Files:** {total}"
        await message.reply(text)
