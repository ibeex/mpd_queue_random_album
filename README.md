mpdrandom
============
Is a script that adds some randomness to mpds albums.

# Features
* Queue albums randomly from the library 

#Installation
	git clone https://github.com/ibeex/mpd_queue_random_album
	cd mpd_queue_random_album
	pipsi install .

#Usage
    usage: mpdrandom [-h] [-p PORT] [-u HOST] [--password PASSWORD] -n
    
    Pick and play a random album from the current playlist
    
    optional arguments:
      -h, --help            show this help message and exit
      -n NUMBER_OFF_ALBUMS, --no NUMBER_OFF_ALBUMS
                            number of albums to queue
      -p PORT, --port PORT  specify mpd's port (defaults to 6600)
      -u HOST, --host HOST  specify mpd's host (defaults to 127.0.0.1)
      --password PASSWORD   specify mpd's password

#Thanks
thanks to [moOde audio player](http://moodeaudio.org/). For great audio player.