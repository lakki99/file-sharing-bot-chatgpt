import os

API_ID = int(os.getenv("API_ID", "22432833"))
API_HASH = os.getenv("API_HASH", "897f1c440892cfc46c7e222dfb37d015")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7746298562:AAEF2LmH02RM-GnbyOiF3_Ws2CLDJBac6iA")
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://eno2223456:7Cdmqig5Ih2vrqW4@cluster0.ccpmee5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_CHANNEL = int(os.getenv("DB_CHANNEL", "-1002609374874"))  # Telegram channel ID

ADMINS = [int(x) for x in os.getenv("ADMINS", "7592041488").split()]  # Space-separated admin user_ids
EXPIRY_MINUTES = int(os.getenv("EXPIRY_MINUTES", "30"))  # Default expiry
