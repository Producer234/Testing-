# Copyright (C) 2025 by PR-all-bots @ Github, < https://github.com/PR-All-Bots >
# All rights reserved. © PriyaMusic.

"""
PriyaMusic is a private Telegram bot project developed for personal use.
Copyright (c) 2025 ~ Present PR-all-bots <https://github.com/PR-All-Bots>

This program is licensed software: you may use and modify it for personal,
non-commercial purposes. Collaboration and improvements are welcome
with proper credit to the original creator.
"""


import random

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from PriyaMusic import app
from PriyaMusic.misc import db
from PriyaMusic.utils.decorators import AdminRightsCheck

# Commands
SHUFFLE_COMMAND = get_command("SHUFFLE_COMMAND")


@app.on_message(filters.command(SHUFFLE_COMMAND) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def admins(Client, message: Message, _, chat_id):
    if len(message.command) != 1:
        return await message.reply_text(_["general_2"])
    check = db.get(chat_id)
    if not check:
        return await message.reply_text(_["admin_21"])
    try:
        popped = check.pop(0)
    except Exception:
        return await message.reply_text(_["admin_22"])
    check = db.get(chat_id)
    if not check:
        check.insert(0, popped)
        return await message.reply_text(_["admin_22"])
    random.shuffle(check)
    check.insert(0, popped)
    await message.reply_text(_["admin_23"].format(message.from_user.first_name))
