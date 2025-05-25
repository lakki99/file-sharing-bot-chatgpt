# bot/database.py

import os
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv

load_dotenv("config.env")

MONGO_URL = os.getenv("MONGO_URL")
DATABASE_CHANNEL_ID = int(os.getenv("DATABASE_CHANNEL_ID"))

client = MongoClient(MONGO_URL)
db = client.file_bot

files_col = db.files
users_col = db.users

async def save_file(client, msg):
    file_data = {
        "user_id": msg.from_user.id,
        "chat_id": msg.chat.id,
        "message_id": msg.id,
        "date": datetime.utcnow(),
        "views": 0,
    }
    result = files_col.insert_one(file_data)

    forward = await msg.forward(DATABASE_CHANNEL_ID)
    link = f"https://t.me/{(await client.get_chat(DATABASE_CHANNEL_ID)).username}/{forward.id}"
    files_col.update_one({"_id": result.inserted_id}, {"$set": {"link": link}})
    return forward

async def get_user_files(user_id, limit=200):
    files = files_col.find({"user_id": user_id}).sort("date", -1).limit(limit)
    result = []
    async for f in files:
        result.append({
            "link": f.get("link"),
            "shortlink": f.get("shortlink", f.get("link")),
        })
    return result

async def update_view(link):
    files_col.update_one({"link": link}, {"$inc": {"views": 1}})

async def get_views(link):
    file = files_col.find_one({"link": link})
    return file["views"] if file else 0
