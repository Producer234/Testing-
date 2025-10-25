# Copyright (C) 2025 by PR-all-bots @ Github, < https://github.com/PR-All-Bots >
# All rights reserved. © PriyaMusic.

"""
PriyaMusic is a private Telegram bot project developed for personal use.
Copyright (c) 2025 ~ Present PR-all-bots <https://github.com/PR-All-Bots>

This program is licensed software: you may use and modify it for personal,
non-commercial purposes. Collaboration and improvements are welcome
with proper credit to the original creator.
"""


from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER(__name__).info("Connecting to your Mongo Database...")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Alexa
    LOGGER(__name__).info("Connected to your Mongo Database.")
except Exception:
    LOGGER(__name__).error("Failed to connect to your Mongo Database.")
    exit()

## Database For Broadcast Subscription By Team PR
MONGODB_CLI = AsyncIOMotorClient(MONGO_DB_URI)
db = MONGODB_CLI["subscriptions"]
