# mpdrandom
Is a script that adds some randomness to mpds albums.

# Features
- Queue albums randomly from the library

# Installation
    git clone https://github.com/ibeex/mpd_queue_random_album
    cd mpd_queue_random_album
    pipsi install .

# Usage
    usage: mpdcontrol [-h] [-p PORT] [-u HOST] [--password PASSWORD] {random,current,search} ...

    positional arguments:
      {random,current,search}
      random              Enqueue random albums
      current             Enqueue album based on song currently played
      search              Search albums by year relesed

    optional arguments:
    -h, --help            show this help message and exit
    -p PORT, --port PORT  specify mpd's port (defaults to 6600)
    -u HOST, --host HOST  specify mpd's host (defaults to 192.168.88.241)
    --password PASSWORD   specify mpd's password

# Thanks
Thanks to [moOde audio player](http://moodeaudio.org/). For great audio player.
