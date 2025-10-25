# Copyright (C) 2025 by PR-all-bots @ Github, < https://github.com/PR-All-Bots >
# All rights reserved. © PriyaMusic.

"""
PriyaMusic is a private Telegram bot project developed for personal use.
Copyright (c) 2025 ~ Present PR-all-bots <https://github.com/PR-All-Bots>

This program is licensed software: you may use and modify it for personal,
non-commercial purposes. Collaboration and improvements are welcome
with proper credit to the original creator.
"""


import asyncio
import importlib
from typing import Any

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from PriyaMusic import LOGGER, app, userbot
from PriyaMusic.core.call import Alexa
from PriyaMusic.misc import sudo
from PriyaMusic.plugins import ALL_MODULES
from PriyaMusic.utils.database import get_banned_users, get_gbanned
from PriyaMusic.core.cookies import save_cookies


async def init() -> None:
    # Check for at least one valid Pyrogram string session
    if all(not getattr(config, f"STRING{i}") for i in range(1, 6)):
        LOGGER("PriyaMusic").error("Add Pyrogram string session and then try...")
        exit()
    await sudo()
    try:
        for user_id in await get_gbanned():
            BANNED_USERS.add(user_id)
        for user_id in await get_banned_users():
            BANNED_USERS.add(user_id)
    except Exception:
        pass
    await app.start()
    await save_cookies()
    for module in ALL_MODULES:
        importlib.import_module(f"PriyaMusic.plugins{module}")
    LOGGER("PriyaMusic.plugins").info("Necessary Modules Imported Successfully.")
    await userbot.start()
    await Priya.start()
    try:
        await Priya.stream_call("https://telegra.ph/file/b60b80ccb06f7a48f68b5.mp4")
    except NoActiveGroupCall:
        LOGGER("PriyaMusic").error(
            "[ERROR] - \n\nTurn on group voice chat and don't put it off otherwise I'll stop working thanks."
        )
        exit()
    except Exception:
        pass
    await Priya.decorators()
    LOGGER("PriyaMusic").info("Priya Music Bot Started Successfully")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("PriyaMusic").info("Stopping Priya Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
    LOGGER("PriyaMusic").info("Stopping Music Bot")
