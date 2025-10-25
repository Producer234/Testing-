# Copyright (C) 2025 by PR-all-bots @ Github, < https://github.com/PR-All-Bots >
# All rights reserved. © PriyaMusic.

"""
PriyaMusic is a private Telegram bot project developed for personal use.
Copyright (c) 2025 ~ Present PR-all-bots <https://github.com/PR-All-Bots>

This program is licensed software: you may use and modify it for personal,
non-commercial purposes. Collaboration and improvements are welcome
with proper credit to the original creator.
"""


from os import listdir, mkdir
from os.path import isdir
from shutil import rmtree

from ..logging import LOGGER


def dirr():
    current_items = listdir()

    if "assets" not in current_items:
        LOGGER(__name__).warning(
            "Assets Folder not Found. Please clone repository again."
        )
        exit()

    for folder in ("downloads", "cache"):
        if folder in current_items and isdir(folder):
            rmtree(folder)
        mkdir(folder)

    LOGGER(__name__).info("Directories Updated.")
