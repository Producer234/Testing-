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

from strings import get_command
from PriyaMusic import app
from PriyaMusic.misc import SUDOERS
from PriyaMusic.utils.database import set_video_limit
from PriyaMusic.utils.decorators.language import language

VIDEOLIMIT_COMMAND = get_command("VIDEOLIMIT_COMMAND")


@app.on_message(filters.command(VIDEOLIMIT_COMMAND) & SUDOERS)
@language
async def set_video_limit_kid(client, message: Message, _):
    if len(message.command) != 2:
        usage = _["vid_1"]
        return await message.reply_text(usage)
    message.chat.id
    state = message.text.split(None, 1)[1].strip()
    if state.lower() == "disable":
        limit = 0
        await set_video_limit(limit)
        return await message.reply_text(_["vid_4"])
    if state.isnumeric():
        limit = int(state)
        await set_video_limit(limit)
        if limit == 0:
            return await message.reply_text(_["vid_4"])
        await message.reply_text(_["vid_3"].format(limit))
    else:
        return await message.reply_text(_["vid_2"])
