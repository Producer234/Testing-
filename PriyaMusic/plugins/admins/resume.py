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
from PriyaMusic.utils.database import is_music_playing, music_on
from PriyaMusic.utils.decorators import AdminRightsCheck

# Commands
RESUME_COMMAND = get_command("RESUME_COMMAND")


@app.on_message(filters.command(RESUME_COMMAND) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if len(message.command) != 1:
        return await message.reply_text(_["general_2"])
    if await is_music_playing(chat_id):
        return await message.reply_text(_["admin_3"], disable_web_page_preview=True)
    await music_on(chat_id)
    await Alexa.resume_stream(chat_id)
    await message.reply_text(
        _["admin_4"].format(message.from_user.mention), disable_web_page_preview=True
    )
