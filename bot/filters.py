from pyrogram import filters
from bot.config import ADMINS
from bot.database import is_verified


def admin_filter(_, __, update):
    return update.from_user and update.from_user.id in ADMINS


def verified_filter(_, __, update):
    return update.from_user and is_verified(update.from_user.id)


admin_filter = filters.create(admin_filter)
verified_filter = filters.create(verified_filter)
