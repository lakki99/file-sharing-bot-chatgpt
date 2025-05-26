import asyncio
from datetime import datetime
from bot.database import files, batches

CLEANUP_INTERVAL = 600  # seconds (10 minutes)

async def cleanup_expired_files():
    while True:
        now_ts = datetime.utcnow().timestamp()

        # Find expired files and batches
        expired_files = list(files.find({"expires_at": {"$lte": now_ts}}))
        expired_batches = list(batches.find({"expires_at": {"$lte": now_ts}}))

        # Delete expired files and batches
        for f in expired_files:
            files.delete_one({"_id": f["_id"]})

        for b in expired_batches:
            batches.delete_one({"_id": b["_id"]})

        await asyncio.sleep(CLEANUP_INTERVAL)

def start_cleanup_job():
    import asyncio
    loop = asyncio.get_event_loop()
    loop.create_task(cleanup_expired_files())
