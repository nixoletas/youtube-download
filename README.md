# youtube-download

Simple CLI to download YouTube videos as MP4 (max resolution) or MP3.

## Requirements

- Python 3.8+
- [ffmpeg](https://ffmpeg.org/download.html) installed and on your `PATH` (needed to merge video/audio and to extract MP3)

## Install

```bash
pip install yt-dlp
```

## Usage

Run the script:

```bash
python yt.py
```

You'll be prompted for:

1. **YouTube link** — paste the video URL
2. **Format** — `mp4` (max resolution, default) or `mp3`
3. **Destination folder** — where to save the file (default: `downloads`)

The downloaded file is named after the video title and saved in the destination folder.

## Example

```
=== YouTube Downloader ===
Cola link do YouTube: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Formato [mp4/mp3] (enter=mp4): mp3
Pasta destino (enter=downloads):

Baixando mp3 em 'downloads'...

Pronto.
```
