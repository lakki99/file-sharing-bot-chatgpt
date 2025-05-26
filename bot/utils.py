import string
import random
from datetime import datetime, timedelta
from bot.config import EXPIRY_MINUTES

def generate_short_id(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

def get_expiry_timestamp():
    return (datetime.utcnow() + timedelta(minutes=EXPIRY_MINUTES)).timestamp()
