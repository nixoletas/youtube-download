#!/usr/bin/env python3
"""CLI simples: cola link do YouTube, baixa em mp4 (resolucao maxima) ou mp3."""

import os
import sys

try:
    from yt_dlp import YoutubeDL
except ImportError:
    sys.exit("yt-dlp nao instalado. Rode: pip install yt-dlp")


def baixar(url: str, formato: str, destino: str) -> None:
    os.makedirs(destino, exist_ok=True)
    saida = os.path.join(destino, "%(title)s.%(ext)s")

    # Permite baixar o solver de JS challenge (assinatura/n) do YouTube.
    # Sem isso o YouTube devolve URLs sem assinar -> HTTP 403.
    base = {
        "outtmpl": saida,
        "remote_components": ["ejs:github"],
    }

    if formato == "mp3":
        opts = {
            **base,
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "0",  # melhor qualidade VBR
            }],
        }
    else:  # mp4 resolucao maxima
        opts = {
            **base,
            "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
        }

    with YoutubeDL(opts) as ydl:
        ydl.download([url])


def main() -> None:
    print("=== YouTube Downloader ===")
    url = input("Cola link do YouTube: ").strip()
    if not url:
        sys.exit("Link vazio.")

    formato = ""
    while formato not in ("mp3", "mp4"):
        formato = input("Formato [mp4/mp3] (enter=mp4): ").strip().lower() or "mp4"
        if formato not in ("mp3", "mp4"):
            print("Escolhe mp3 ou mp4.")

    destino = input("Pasta destino (enter=downloads): ").strip() or "downloads"

    print(f"\nBaixando {formato} em '{destino}'...\n")
    try:
        baixar(url, formato, destino)
    except Exception as e:
        sys.exit(f"Erro: {e}")
    print("\nPronto.")


if __name__ == "__main__":
    main()
