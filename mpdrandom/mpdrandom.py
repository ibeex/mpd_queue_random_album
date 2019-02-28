#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import json
import random
from argparse import ArgumentParser
from pathlib import Path
from typing import List, Optional

import mpd

# Default Server info, change these values to match yours.
HOST = "192.168.88.241"
PORT = "6600"
PASSWORD = None

__version__ = "1.0.0"
__author__ = "IbeeX"


def queue_random_album(client: mpd.MPDClient, cache: List[str]) -> Optional[str]:

    albums: List[str] = client.list("album")
    while True:
        album_name = random.choice(albums)
        if not album_name:
            return None
        if album_name in cache:
            print(f"{album_name}, album was queaed recently skipping...")
            continue
        break
    client.findadd("album", album_name)
    album = client.find("album", album_name)[0]
    if "albumartist" in album:
        print(f"{album['albumartist']}: {album['album']}, from {len(albums)} albums.")
    else:
        print(f"{album['artist']}: {album['album']}, from {len(albums)} albums.")
    return album_name


def enforce_cache_size(size: int, cache: List[str]) -> List[str]:
    if len(cache) > size:
        return cache[len(cache) - size :]
    return cache


def get_cache_size(no_albums: int, percent: int = 10) -> int:
    cache_size: int = int(no_albums / 100 * percent)
    if no_albums <= 1:
        cache_size = 0
    elif cache_size == 0:
        cache_size = 1
    elif cache_size > 100:
        cache_size = 100
    return cache_size


def get_cache_file() -> Path:
    cache_dir = Path.home() / ".cache" / "mpdrandom"
    cache_dir.mkdir(parents=True, exist_ok=True)
    return cache_dir / "cache.json"


def load_cache(cache_file: Path) -> List[str]:
    json_cache: str = ""
    if not cache_file.is_file():
        return []
    with cache_file.open() as f:
        json_cache = f.read()
    return json.loads(json_cache)


def save_cache(cache_file, cache):
    with cache_file.open(mode="w") as f:
        f.write(json.dumps(cache, indent=4, sort_keys=True))


def enqueue_current(client: mpd.MPDClient) -> None:
    song = client.currentsong()
    client.findadd("album", song["album"])


def main(args):
    client = mpd.MPDClient()
    client.timeout = 10
    client.idletimeout = None
    client.connect(args.host, args.port)
    if args.password:
        client.password(args.password)
    if args.enque_current:
        enqueue_current(client)
    else:
        cache_file = get_cache_file()
        cache = load_cache(cache_file)
        albums: List[str] = client.list("album")
        percent = get_cache_size(len(albums))
        for n in range(args.number_off_albums):
            album_name = queue_random_album(client, cache)
            if not album_name:
                break
            cache.append(album_name)
            cache = enforce_cache_size(percent, cache)
        save_cache(cache_file, cache)
    client.close()
    client.disconnect()


def cli():
    arguments = ArgumentParser(
        description="Pick and play a random album from " "the current playlist"
    )
    arguments.add_argument(
        "-n",
        "--no",
        type=int,
        dest="number_off_albums",
        default=1,
        help="number of albums to queue",
    )
    arguments.add_argument(
        "-c",
        "--current",
        type=bool,
        dest="enque_current",
        default=False,
        help="enque album from current song",
    )
    arguments.add_argument(
        "-p",
        "--port",
        dest="port",
        default=PORT,
        help="specify mpd's port (defaults to {})".format(PORT),
        metavar="PORT",
    )
    arguments.add_argument(
        "-u",
        "--host",
        dest="host",
        default=HOST,
        help="specify mpd's host (defaults to {})".format(HOST),
        metavar="HOST",
    )
    arguments.add_argument(
        "--password",
        dest="password",
        default=PASSWORD,
        help="specify mpd's password",
        metavar="PASSWORD",
    )
    args = arguments.parse_args()

    main(args)
