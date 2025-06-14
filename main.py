import argparse
import os
from yt_dlp import YoutubeDL


def download(url: str, output_dir: str) -> None:
    """Download a single URL as an MP3 file."""
    os.makedirs(output_dir, exist_ok=True)
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Download audio from URLs as MP3 using yt-dlp"
    )
    parser.add_argument("urls", nargs="+", help="URLs to download")
    parser.add_argument(
        "-o",
        "--output",
        default="downloads",
        help="Output directory for downloaded files",
    )
    args = parser.parse_args()
    for url in args.urls:
        download(url, args.output)


if __name__ == "__main__":
    main()
