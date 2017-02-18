# pmcli - (p)lay (m)usic for (cli)

Browse and stream Google Play Music from the command line

## Dependencies

- [Python 3](https://www.python.org/downloads/)
- [mpv](mpv.io)
- [gmusicapi](https://github.com/simon-weber/gmusicapi): `pip install gmusicapi`

## Installation

```sh
git clone https://github.com/christopher-dG/pmcli
cd pmcli
```

Now, edit `config` with your Google account information. Next:

```sh
cp config mpv_input.conf ~/.config/pmcli
cp src ~/.local/share/pmcli
chmod +x ~/.local/share/pmcli/src/pmcli.py
ln -s /usr/local/bin/pmcli ~/.local/share/pmcli/pmcli.py
```

## Device ID
If you don't know your device ID, run `python script/get_dev_id.py` and answer the prompts to generate a list of valid device IDs.

## Running pmcli
Once installed, the program can be run with `pmcli`.

## Controls
- `s/search search-term`: Search for 'search-term'`
- `e/expand 123`: Expand item number 123
- `p/play`: Play current queue
-  `p/play s`: Shuffle and play current queue
- `p/play 123`: Play item number 123
- `q/queue`: Show current queue
- `q/queue 123`:  Add item number 123 to queue
- `w/write file-name`: Write current queue to file file-name
- `r/restore file-name`: Replace current queue with playlist from file-name
- `h/help`: Show help message
- `Ctrl-C`: Exit pmcli

When playing music:
- `spc`: Play/pause
- `9/0`: Volume down/up (Note: volume changes do not persist across songs, so I recommend you adjust your system volume instead)
- `n`: Next track
- `q`: Stop

## Todo
- Properly display shuffled queue
- Restore queue from shuffle
- Seek backwards function
- Colour support
- Text-only debugging UI
- Add threading support (play in background and keep browsing)
- Caching queue contents for seamless transitions (save locally and delete after? Probably needs threading)
