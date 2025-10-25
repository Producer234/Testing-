# Copyright (C) 2025 by PR-all-bots @ Github, < https://github.com/PR-All-Bots >
# All rights reserved. © PriyaMusic.

"""
PriyaMusic is a private Telegram bot project developed for personal use.
Copyright (c) 2025 ~ Present PR-all-bots <https://github.com/PR-All-Bots>

This program is licensed software: you may use and modify it for personal,
non-commercial purposes. Collaboration and improvements are welcome
with proper credit to the original creator.
"""


from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from PriyaMusic import app
from PriyaMusic.core.call import Alexa
from PriyaMusic.utils.database import is_muted, mute_off
from PriyaMusic.utils.decorators import AdminRightsCheck

# Commands
UNMUTE_COMMAND = get_command("UNMUTE_COMMAND")


@app.on_message(filters.command(UNMUTE_COMMAND) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def unmute_admin(Client, message: Message, _, chat_id):
    if len(message.command) != 1 or message.reply_to_message:
        return await message.reply_text(_["general_2"])
    if not await is_muted(chat_id):
        return await message.reply_text(_["admin_7"], disable_web_page_preview=True)
    await mute_off(chat_id)
    await Priya.unmute_stream(chat_id)
    await message.reply_text(
        _["admin_8"].format(message.from_user.mention), disable_web_page_preview=True
    )
