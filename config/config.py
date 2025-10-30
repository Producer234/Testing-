# Copyright (C) 2025 by PR-all-bots @ Github, < https://github.com/PR-All-Bots >
# All rights reserved. © PriyaMusic.

"""
PriyaMusic is a private Telegram bot project developed for personal use.
Copyright (c) 2025 ~ Present PR-all-bots <https://github.com/PR-All-Bots>

This program is licensed software: you may use and modify it for personal,
non-commercial purposes. Collaboration and improvements are welcome
with proper credit to the original creator.
"""

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")

MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-4923861675"))

MUSIC_BOT_NAME = getenv("PRIYA MUSIC ")

OWNER_ID = int(getenv("OWNER_ID", None))

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

BOT_ID = getenv("BOT_ID")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/TheTeamAlexa/AlexaMusic")

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/PR_ALL_BOT")

SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/PR_ALL_BOT_SUPPORT")

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")

AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "11500"))

AUTO_SUGGESTION_TIME = int(getenv("AUTO_SUGGESTION_TIME", "5400"))

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "False")

PRIVATE_BOT_MODE = getenv("PR", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))

TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))

CHANNEL = getenv("CHANNEL", "https://t.me/MAIN_CHANNEL_PR")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", 8c64fb11c993401ab5b1668c411cabbd)

SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", 4235f347a80d437a846544e005e6fa02)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "2"))

SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "7"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))

TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

COOKIES = getenv("COOKIES", None)
# https://batbin.me/titivil

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://envs.sh/CK4.jpg"
)

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "assets/Ping.jpeg",
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "assets/Playlist.jpeg",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "assets/Global.jpeg",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "assets/Stats.jpeg",
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "assets/Audio.jpeg",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "assets/Video.jpeg",
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "assets/Stream.jpeg",
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "assets/Soundcloud.jpeg",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "assets/Youtube.jpeg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "assets/SpotifyArtist.jpeg",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "assets/SpotifyAlbum.jpeg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "assets/SpotifyPlaylist.jpeg",
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    print(
        "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()

if SUPPORT_GROUP and not re.match("(?:http|https)://", SUPPORT_GROUP):
    print(
        "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()

if UPSTREAM_REPO and not re.match("(?:http|https)://", UPSTREAM_REPO):
    print(
        "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()


if (
    PING_IMG_URL
    and PING_IMG_URL != "assets/Ping.jpeg"
    and not re.match("(?:http|https)://", PING_IMG_URL)
):
    print(
        "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()

if (
    PLAYLIST_IMG_URL
    and PLAYLIST_IMG_URL != "assets/Playlist.jpeg"
    and not re.match("(?:http|https)://", PLAYLIST_IMG_URL)
):
    print(
        "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()

if (
    GLOBAL_IMG_URL
    and GLOBAL_IMG_URL != "assets/Global.jpeg"
    and not re.match("(?:http|https)://", GLOBAL_IMG_URL)
):
    print(
        "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()


if STATS_IMG_URL and (
    STATS_IMG_URL != "assets/Stats.jpeg"
    and not re.match("(?:http|https)://", STATS_IMG_URL)
):
    print(
        "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()


if (
    TELEGRAM_AUDIO_URL
    and TELEGRAM_AUDIO_URL != "assets/Audio.jpeg"
    and not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL)
):
    print(
        "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()


if (
    STREAM_IMG_URL
    and STREAM_IMG_URL != "assets/Stream.jpeg"
    and not re.match("(?:http|https)://", STREAM_IMG_URL)
):
    print(
        "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()


if (
    SOUNCLOUD_IMG_URL
    and SOUNCLOUD_IMG_URL != "assets/Soundcloud.jpeg"
    and not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL)
):
    print(
        "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()

if (
    YOUTUBE_IMG_URL
    and YOUTUBE_IMG_URL != "assets/Youtube.jpeg"
    and not re.match("(?:http|https)://", YOUTUBE_IMG_URL)
):
    print(
        "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()


if (
    TELEGRAM_VIDEO_URL
    and TELEGRAM_VIDEO_URL != "assets/Video.jpeg"
    and not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL)
):
    print(
        "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()
