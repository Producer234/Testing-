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
from PriyaMusic import app
from pyrogram import Client, filters
from datetime import datetime, timedelta
from pyrogram.errors import FloodWait
from PriyaMusic.core.mongo import db as alexa
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PriyaMusic.utils.database import get_served_users, get_served_chats


OWNER_ID = 7753899951
