# YouTube Video Downloader

A powerful and feature-rich Python script for downloading YouTube videos with multiple quality options, audio extraction, and playlist support.

## Features

- **Multiple Download Options**:
  - Download videos with quality selection
  - Download audio only (MP3 format)
  - Download in best available quality
  - Download entire playlists

- **Quality Selection**:
  - View available video formats
  - Choose specific video quality
  - See file sizes before downloading
  - Automatic fallback to best quality if selection fails

- **Audio Download**:
  - Extract audio from videos
  - Convert to MP3 format
  - High-quality audio (192kbps)
  - Preserve original audio quality

- **Playlist Support**:
  - Download entire playlists
  - Shows number of videos in playlist
  - Confirmation prompt before playlist download
  - Progress tracking for multiple downloads

- **User-Friendly Interface**:
  - Interactive command-line interface
  - Real-time download progress
  - Clear error messages
  - Detailed troubleshooting tips

## Requirements

- Python 3.7 or higher
- FFmpeg (for audio conversion)
- Required Python packages:
  ```
  yt-dlp==2024.3.10
  tqdm==4.66.2
  ```

## Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/Shyam1092/YouTube_Video_Downloader]
   cd youtube-downloader
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Install FFmpeg:
   - Windows: Download from [FFmpeg website](https://ffmpeg.org/download.html)
   - Linux: `sudo apt-get install ffmpeg`
   - macOS: `brew install ffmpeg`

## Usage

1. Run the script:
   ```bash
   python youtube_downloader.py
   ```

2. Enter a YouTube URL when prompted

3. Choose download option:
   - Option 1: Download video with quality selection
   - Option 2: Download audio only (MP3)
   - Option 3: Download best quality

4. For quality selection:
   - View available formats
   - Enter the number of your preferred format
   - Or press Enter for best quality

5. For playlists:
   - Enter playlist URL
   - Confirm to download all videos
   - Monitor progress for each video

## Examples

```bash
# Download video with quality selection
Enter YouTube URL: https://www.youtube.com/watch?v=example
Enter your choice (1-3): 1

# Download audio only
Enter YouTube URL: https://www.youtube.com/watch?v=example
Enter your choice (1-3): 2

# Download playlist
Enter YouTube URL: https://www.youtube.com/playlist?list=example
Enter your choice (1-3): 3
```

## Troubleshooting

If you encounter any issues:

1. Make sure you have a stable internet connection
2. Update yt-dlp: `pip install --upgrade yt-dlp`
3. Check if the video is available in your region
4. Verify you have enough disk space
5. Run the script as administrator
6. Check if your antivirus is blocking the download

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer

This tool is for educational purposes only. Please respect YouTube's terms of service and copyright laws when downloading videos. 
