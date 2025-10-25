# Copyright (C) 2025 by PR-all-bots @ Github, < https://github.com/PR-All-Bots >
# All rights reserved. © PriyaMusic.

"""
PriyaMusic is a private Telegram bot project developed for personal use.
Copyright (c) 2025 ~ Present PR-all-bots <https://github.com/PR-All-Bots>

This program is licensed software: you may use and modify it for personal,
non-commercial purposes. Collaboration and improvements are welcome
with proper credit to the original creator.
"""

from typing import Dict, List, Union

from PriyaMusic.core.mongo import mongodb


pmpermitdb = mongodb.permit


async def is_pmpermit_approved(user_id: int) -> bool:
    user = await pmpermitdb.find_one({"user_id": user_id})
    return bool(user)


async def approve_pmpermit(user_id: int):
    is_pmpermit = await is_pmpermit_approved(user_id)
    if is_pmpermit:
        return
    return await pmpermitdb.insert_one({"user_id": user_id})


async def disapprove_pmpermit(user_id: int):
    is_pmpermit = await is_pmpermit_approved(user_id)
    if not is_pmpermit:
        return
    return await pmpermitdb.delete_one({"user_id": user_id})
