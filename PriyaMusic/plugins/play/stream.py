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
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from strings import get_command
from PriyaMusic import app
from PriyaMusic.core.call import Priya
from PriyaMusic.utils.decorators.play import PlayWrapper
from PriyaMusic.utils.logger import play_logs
from PriyaMusic.utils.stream.stream import stream

# Command
STREAM_COMMAND = get_command("STREAM_COMMAND")


@app.on_message(filters.command(STREAM_COMMAND) & filters.group & ~BANNED_USERS)
@PlayWrapper
async def stream_command(
    client,
    message: Message,
    _,
    chat_id,
    video,
    channel,
    playmode,
    url,
    fplay,
):
    if url:
        mystic = await message.reply_text(
            _["play_2"].format(channel) if channel else _["play_1"]
        )
        try:
            await Alexa.stream_call(url)
        except NoActiveGroupCall:
            await mystic.edit_text(
                "ᴛʜᴇʀᴇ's ᴀɴ ɪssᴜᴇ ᴡɪᴛʜ ᴛʜᴇ ʙᴏᴛ. ᴘʟᴇᴀsᴇ ʀᴇᴘᴏʀᴛ ɪᴛ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ ᴀɴᴅ ᴀsᴋ ᴛʜᴇᴍ ᴛᴏ ᴄʜᴇᴄᴋ ʟᴏɢɢᴇʀ ɢʀᴏᴜᴘ."
            )
            return await app.send_message(
                config.LOG_GROUP_ID,
                "ᴘʟᴇᴀsᴇ ᴛᴜʀɴ ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.. ʙᴏᴛ ɪs ɴᴏᴛ ᴀʙʟᴇ ᴛᴏ sᴛʀᴇᴀᴍ ᴜʀʟs..",
            )
        except Exception as e:
            return await mystic.edit_text(_["general_3"].format(type(e).__name__))
        await mystic.edit_text(_["str_2"])
        try:
            await stream(
                _,
                mystic,
                message.from_user.id,
                url,
                chat_id,
                message.from_user.first_name,
                message.chat.id,
                video=True,
                streamtype="index",
            )
        except Exception as e:
            ex_type = type(e).__name__
            err = e if ex_type == "AssistantErr" else _["general_3"].format(ex_type)
            return await mystic.edit_text(err)
        return await play_logs(message, streamtype="M3u8 or Index Link")
    else:
        await message.reply_text(_["str_1"])
