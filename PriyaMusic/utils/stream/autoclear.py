# Copyright (C) 2025 by PR-all-bots @ Github, < https://github.com/PR-All-Bots >
# All rights reserved. © PriyaMusic.

"""
PriyaMusic is a private Telegram bot project developed for personal use.
Copyright (c) 2025 ~ Present PR-all-bots <https://github.com/PR-All-Bots>

This program is licensed software: you may use and modify it for personal,
non-commercial purposes. Collaboration and improvements are welcome
with proper credit to the original creator.
"""

import os

import asyncio
from config import autoclean


async def auto_clean(popped):
    async def _auto_clean(popped_item):
        try:
            rem = popped_item.get("file")
            if rem:
                autoclean.discard(rem)
                if all(keyword not in rem for keyword in ("vid_", "live_", "index_")):
                    try:
                        os.remove(rem)
                    except FileNotFoundError:
                        pass
        except Exception:
            pass

    if isinstance(popped, dict):
        await _auto_clean(popped)
    elif isinstance(popped, list):
        await asyncio.gather(*(_auto_clean(pop) for pop in popped))
    else:
        raise ValueError("Expected popped to be a dict or list.")
