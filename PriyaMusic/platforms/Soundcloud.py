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
from os import path

from yt_dlp import YoutubeDL

from PriyaMusic.utils.formatters import seconds_to_min


class SoundAPI:
    def __init__(self):
        self.opts = {
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "format": "bestaudio[ext=m4a]/bestaudio/best",
            "retries": 3,
            "nooverwrites": False,
            "continuedl": True,
            "quiet": True,
        }

    async def valid(self, link: str):
        return "soundcloud" in link and "sets" not in link

    async def download(self, url):
        d = YoutubeDL(self.opts)
        try:
            info = await asyncio.to_thread(d.extract_info, url)
        except Exception as e:
            print(f"Error: {e}")
            return False
        xyz = path.join("downloads", f"{info['id']}.{info['ext']}")
        duration_min = seconds_to_min(info["duration"])
        track_details = {
            "title": info["title"],
            "duration_sec": info["duration"],
            "duration_min": duration_min,
            "uploader": info["uploader"],
            "filepath": xyz,
        }
        return track_details, xyz
