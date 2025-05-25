# bot/shortlink.py

import aiohttp
import os
from dotenv import load_dotenv

load_dotenv("config.env")

SHORTLINK_API = os.getenv("SHORTLINK_API")
SHORTLINK_URL = os.getenv("SHORTLINK_URL")

async def generate_shortlink(original_url: str) -> str:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{SHORTLINK_URL}?api={SHORTLINK_API}&url={original_url}"
            ) as response:
                data = await response.json()
                if data["status"] == "success":
                    return data["shortenedUrl"]
                else:
                    return original_url
    except Exception as e:
        print(f"Shortlink generation failed: {e}")
        return original_url
