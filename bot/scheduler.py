# bot/scheduler.py

import asyncio
from pyrogram import Client
from pyrogram.errors import MessageDeleteForbidden

async def schedule_deletion(client: Client, chat_id: int, message_id: int, user_id: int):
    await asyncio.sleep(1800)  # 30 minutes

    try:
        await client.delete_messages(chat_id, message_id)
        await client.send_message(user_id, "Your file/message has been automatically deleted after 30 minutes.")
    except MessageDeleteForbidden:
        await client.send_message(user_id, "Couldn't delete the file. I may lack delete permissions.")
    except Exception as e:
        print(f"Error deleting message: {e}")
