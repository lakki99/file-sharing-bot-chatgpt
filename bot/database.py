from pymongo import MongoClient, ASCENDING
from datetime import datetime
from bot.config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client.file_share_bot

# Collections
users = db.users
files = db.files
batches = db.batches

# User functions
def add_user(user_id):
    users.update_one({"_id": user_id}, {"$setOnInsert": {"verified": False}}, upsert=True)

def is_admin(user_id):
    from bot.config import ADMINS
    return user_id in ADMINS

def is_verified(user_id):
    data = users.find_one({"_id": user_id})
    return data and data.get("verified", False)

def verify_user(user_id):
    users.update_one({"_id": user_id}, {"$set": {"verified": True}}, upsert=True)

# File functions
def save_file(file_id, short_id, expiry_ts, uploader_id):
    files.insert_one({
        "_id": short_id,
        "file_id": file_id,
        "expires_at": expiry_ts,
        "clicks": 0,
        "uploader": uploader_id,
        "type": "file"
    })

def get_file_by_short_id(short_id):
    return files.find_one({"_id": short_id, "type": "file"})

def increase_click(short_id):
    files.update_one({"_id": short_id}, {"$inc": {"clicks": 1}})

# Batch functions
def save_batch(start_msg_id, end_msg_id, short_id, uploader_id):
    batches.insert_one({
        "_id": short_id,
        "start_msg_id": start_msg_id,
        "end_msg_id": end_msg_id,
        "clicks": 0,
        "uploader": uploader_id,
        "type": "batch"
    })

def get_batch_by_short_id(short_id):
    return batches.find_one({"_id": short_id})

def increase_batch_click(short_id):
    batches.update_one({"_id": short_id}, {"$inc": {"clicks": 1}})

# Stats
def get_top_files(limit=10):
    return list(files.find().sort("clicks", -1).limit(limit))

def count_all_files():
    return files.count_documents({})
