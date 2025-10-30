# Copyright (C) 2025 by PR-all-bots @ Github, < https://github.com/PR-All-Bots >
# All rights reserved. © PriyaMusic.

"""
PriyaMusic is a private Telegram bot project developed for personal use.
Copyright (c) 2025 ~ Present PR-all-bots <https://github.com/PR-All-Bots>

This program is licensed software: you may use and modify it for personal,
non-commercial purposes. Collaboration and improvements are welcome
with proper credit to the original creator.
"""

import sys
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
import config
from custom_logger import LOGGER
from spotify_api import get_track  # your Spotify API integration


class PriyaBot(Client):
    def __init__(self):
        super().__init__(
            "MusicBot",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            max_concurrent_transmissions=5,
        )
        LOGGER(__name__).info("Starting Bot...")

    async def start(self):
        await super().start()

        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        self.mention = get_me.mention

        try:
            await self.send_message(config.LOG_GROUP_ID, "» Bot started! Waiting for commands...")
        except Exception:
            LOGGER(__name__).error(
                "Bot failed to access log Group. Add bot to log channel and promote as admin."
            )
            sys.exit()

        member = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if member.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error("Promote Bot as Admin in Logger Group")
            sys.exit()

        self.name = f"{get_me.first_name} {get_me.last_name}" if get_me.last_name else get_me.first_name
        LOGGER(__name__).info(f"Bot Started as {self.name}")

    async def search_spotify(self, track_name):
        track = get_track(track_name)
        if track:
            return f"🎵 Track: {track['name']}\n👤 Artist: {track['artist']}\n🔗 Link: {track['url']}"
        return "No track found."


# Initialize bot instance (do not call run() here)
bot = PriyaBot()


# Spotify command handler
@bot.on_message(filters.command("spotify") & filters.private)
async def spotify_command(client, message):
    query = " ".join(message.command[1:])
    if not query:
        await message.reply_text(
            "Please provide a song name.\nUsage: /spotify Shape of You"
        )
        return

    result = await client.search_spotify(query)
    await message.reply_text(result)
