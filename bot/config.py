import os

API_ID = int(os.getenv("API_ID", "123456"))
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")
MONGO_URI = os.getenv("MONGO_URI", "your_mongodb_uri")
DB_CHANNEL = int(os.getenv("DB_CHANNEL", "-1001234567890"))  # Telegram channel ID

ADMINS = [int(x) for x in os.getenv("ADMINS", "").split()]  # Space-separated admin user_ids
EXPIRY_MINUTES = int(os.getenv("EXPIRY_MINUTES", "30"))  # Default expiry
