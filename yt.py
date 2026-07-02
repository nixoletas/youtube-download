#!/usr/bin/env python3
"""Simple CLI: paste a YouTube link, download as mp4 (max resolution) or mp3."""

import os
import sys

try:
    from yt_dlp import YoutubeDL
except ImportError:
    sys.exit("yt-dlp not installed. Run: pip install yt-dlp")

VALID_FORMATS = ("mp4", "mp3")


def build_options(formato: str, outtmpl: str) -> dict:
    base = {
        "outtmpl": outtmpl,
        # Lets yt-dlp fetch YouTube's JS challenge solver (signature/n param).
        # Without it YouTube returns unsigned URLs -> HTTP 403.
        "remote_components": ["ejs:github"],
    }

    if formato == "mp3":
        return {
            **base,
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "0",  # best VBR quality
            }],
        }

    return {
        **base,
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
    }


def baixar(url: str, formato: str, destino: str) -> None:
    os.makedirs(destino, exist_ok=True)
    outtmpl = os.path.join(destino, "%(title)s.%(ext)s")
    opts = build_options(formato, outtmpl)

    with YoutubeDL(opts) as ydl:
        ydl.download([url])


def prompt_formato() -> str:
    formato = ""
    while formato not in VALID_FORMATS:
        formato = input("Format [mp4/mp3] (enter=mp4): ").strip().lower() or "mp4"
        if formato not in VALID_FORMATS:
            print("Choose mp3 or mp4.")
    return formato


def main() -> None:
    print("=== YouTube Downloader ===")
    url = input("Paste the YouTube link: ").strip()
    if not url:
        sys.exit("Empty link.")

    formato = prompt_formato()
    destino = input("Destination folder (enter=downloads): ").strip() or "downloads"

    print(f"\nDownloading {formato} to '{destino}'...\n")
    try:
        baixar(url, formato, destino)
    except Exception as e:
        sys.exit(f"Error: {e}")
    print("\nDone.")


if __name__ == "__main__":
    main()
