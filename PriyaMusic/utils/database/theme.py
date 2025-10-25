# Copyright (C) 2025 by PR-all-bots @ Github, < https://github.com/PR-All-Bots >
# All rights reserved. © PriyaMusic.

"""
PriyaMusic is a private Telegram bot project developed for personal use.
Copyright (c) 2025 ~ Present PR-all-bots <https://github.com/PR-All-Bots>

This program is licensed software: you may use and modify it for personal,
non-commercial purposes. Collaboration and improvements are welcome
with proper credit to the original creator.
"""


# from typing import Dict, List, Union
# from PriyaMusic.core.mongo import mongodb

# themedb = mongodb.notes


# async def _get_theme(chat_id: int) -> Dict[str, int]:
#     _notes = await themedb.find_one({"chat_id": chat_id})
#     if not _notes:
#         return {}
#     return _notes["notes"]


# async def get_theme(chat_id: int, name: str) -> Union[bool, dict]:
#     name = name.lower().strip()
#     _notes = await _get_theme(chat_id)
#     if name in _notes:
#         return _notes[name]
#     else:
#         return False


# async def save_theme(chat_id: int, name: str, note: dict):
#     name = name.lower().strip()
#     _notes = await _get_theme(chat_id)
#     _notes[name] = note
#     await themedb.update_one(
#         {"chat_id": chat_id}, {"$set": {"notes": _notes}}, upsert=True
#     )
