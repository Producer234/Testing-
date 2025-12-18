from typing import Union
import os

from pyrogram.types import InlineKeyboardButton

from config import CHANNEL, SUPPORT_CHANNEL, SUPPORT_GROUP, OWNER_ID
from PriyaMusic import app


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?start=help",
            ),
            InlineKeyboardButton(text=_["S_B_2"], callback_data="settings_helper"),
        ],
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"),
                InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_GROUP}"),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [InlineKeyboardButton(text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}")]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_GROUP}")]
            )
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [InlineKeyboardButton(text=_["S_B_8"], callback_data="settings_back_helper")]
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"),
                InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_GROUP}"),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [InlineKeyboardButton(text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}")]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_GROUP}")]
            )
    buttons.append(
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ]
    )
    
    # Get owner ID from various sources
    owner_id_to_use = None
    
    # First priority: Use the OWNER parameter passed to function
    if OWNER:
        owner_id_to_use = OWNER
    
    # Second priority: Try environment variable (Heroku)
    if owner_id_to_use is None:
        env_owner_id = os.environ.get("OWNER_ID")
        if env_owner_id:
            try:
                owner_id_to_use = int(env_owner_id.strip())
            except (ValueError, AttributeError):
                pass
    
    # Third priority: Try config.OWNER_ID
    if owner_id_to_use is None and OWNER_ID is not None:
        if isinstance(OWNER_ID, list) and len(OWNER_ID) > 0:
            owner_id_to_use = OWNER_ID[0]
        elif isinstance(OWNER_ID, int):
            owner_id_to_use = OWNER_ID
        else:
            try:
                owner_id_to_use = int(OWNER_ID)
            except (ValueError, TypeError):
                owner_id_to_use = None
    
    if CHANNEL and owner_id_to_use:
        buttons.append(
            [
                InlineKeyboardButton(text=_["S_B_7"], user_id=owner_id_to_use),
                InlineKeyboardButton(text=_["S_B_6"], url=f"{CHANNEL}"),
            ]
        )
    else:
        if CHANNEL:
            buttons.append(
                [
                    InlineKeyboardButton(text=_["S_B_6"], url=f"{CHANNEL}"),
                ]
            )
        if owner_id_to_use:
            buttons.append(
                [
                    InlineKeyboardButton(text=_["S_B_7"], user_id=owner_id_to_use),
                ]
            )
    return buttons


def help_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?start=help",
            ),
            InlineKeyboardButton(text=_["S_B_2"], callback_data="settings_helper"),
        ],
    ]
    return buttons
