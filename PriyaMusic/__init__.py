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
import sys

from PriyaMusic.core.bot import PriyaBot
from PriyaMusic.core.dir import dirr
from PriyaMusic.core.git import git
from PriyaMusic.core.userbot import Userbot
from PriyaMusic.misc import dbb, heroku

from .logging import LOGGER


if sys.platform != "win32":
    try:
        import uvloop
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
        LOGGER(__name__).info("Using Uvloop Event Loop for Enhanced Performance")
    except ImportError:
        LOGGER(__name__).warning("Uvloop not found, using default event loop.")

# ✅ Ensure event loop exists before starting bots
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Bot Client
app = PriyaBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
