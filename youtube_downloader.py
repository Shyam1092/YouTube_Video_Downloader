import yt_dlp
import os
import sys
from tqdm import tqdm

def get_video_formats(url):
    """Get available formats for the video"""
    try:
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = []
            for f in info['formats']:
                if f.get('format_note') and f.get('ext'):
                    formats.append({
                        'format_id': f['format_id'],
                        'ext': f['ext'],
                        'format_note': f['format_note'],
                        'filesize': f.get('filesize', 'Unknown'),
                        'format': f['format']
                    })
            return formats
    except Exception as e:
        print(f"Error getting formats: {str(e)}")
        return []

def show_progress_hook(d):
    """Show download progress"""
    if d['status'] == 'downloading':
        total = d.get('total_bytes', 0)
        downloaded = d.get('downloaded_bytes', 0)
        if total > 0:
            percentage = (downloaded / total) * 100
            print(f"\rDownloading: {percentage:.1f}%", end='')
    elif d['status'] == 'finished':
        print("\nProcessing...")

def download_video(url, format_id=None, audio_only=False, playlist=False):
    try:
        # Base options
        options = {
            'outtmpl': '%(title)s.%(ext)s',
            'quiet': False,
            'no_warnings': True,
            'extract_flat': False,
            'force_generic_extractor': False,
            'nocheckcertificate': True,
            'ignoreerrors': True,
            'socket_timeout': 30,
            'retries': 10,
            'fragment_retries': 10,
            'file_access_retries': 10,
            'extractor_retries': 10,
            'verbose': True,
            'progress_hooks': [show_progress_hook],
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-us,en;q=0.5',
                'Sec-Fetch-Mode': 'navigate',
            }
        }

        if audio_only:
            options['format'] = 'bestaudio/best'
            options['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        elif format_id:
            options['format'] = format_id
        else:
            options['format'] = 'best'

        if playlist:
            options['extract_flat'] = 'in_playlist'
            options['quiet'] = True

        print("\nStarting download...")
        print(f"URL: {url}")
        
        with yt_dlp.YoutubeDL(options) as ydl:
            try:
                # First try to extract info
                print("\nExtracting information...")
                info = ydl.extract_info(url, download=False)
                
                if playlist:
                    print(f"\nFound playlist: {info.get('title', 'Unknown')}")
                    print(f"Number of videos: {len(info.get('entries', []))}")
                    confirm = input("Do you want to download the entire playlist? (y/n): ")
                    if confirm.lower() != 'y':
                        print("Download cancelled.")
                        return
                
                # Then download
                print("\nStarting download...")
                ydl.download([url])
                
            except Exception as e:
                print(f"\nError during download: {str(e)}")
                if not audio_only and not format_id:
                    print("\nTrying alternative format...")
                    options['format'] = 'bestvideo+bestaudio/best'
                    with yt_dlp.YoutubeDL(options) as ydl2:
                        ydl2.download([url])
            
        print("\nDownload completed successfully!")
        
    except Exception as e:
        print(f"\nError: {str(e)}")
        print("\nTroubleshooting tips:")
        print("1. Make sure you have a stable internet connection")
        print("2. Try updating yt-dlp: pip install --upgrade yt-dlp")
        print("3. Check if the video is available in your region")
        print("4. Try a different video URL")
        print("5. Make sure you have enough disk space")
        print("6. Try running the script as administrator")
        print("7. Check if your antivirus is blocking the download")
        sys.exit(1)

def main():
    print("YouTube Video Downloader")
    print("=======================")
    
    while True:
        try:
            url = input("\nEnter YouTube URL (or 'q' to quit): ").strip()
            
            if url.lower() == 'q':
                break
                
            if not url:
                print("Please enter a valid URL")
                continue
                
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url

            # Check if it's a playlist
            is_playlist = 'playlist' in url or '&list=' in url
            
            # Get download options
            print("\nDownload Options:")
            print("1. Download video with quality selection")
            print("2. Download audio only (MP3)")
            print("3. Download best quality")
            
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == '1':
                # Get available formats
                formats = get_video_formats(url)
                if formats:
                    print("\nAvailable formats:")
                    for i, fmt in enumerate(formats, 1):
                        print(f"{i}. {fmt['format_note']} ({fmt['ext']}) - Size: {fmt['filesize']}")
                    
                    format_choice = input("\nEnter format number (or press Enter for best quality): ").strip()
                    if format_choice.isdigit() and 1 <= int(format_choice) <= len(formats):
                        format_id = formats[int(format_choice)-1]['format_id']
                        download_video(url, format_id=format_id, playlist=is_playlist)
                    else:
                        download_video(url, playlist=is_playlist)
                else:
                    print("Could not get format list. Downloading best quality...")
                    download_video(url, playlist=is_playlist)
            
            elif choice == '2':
                download_video(url, audio_only=True, playlist=is_playlist)
            
            elif choice == '3':
                download_video(url, playlist=is_playlist)
            
            else:
                print("Invalid choice. Downloading best quality...")
                download_video(url, playlist=is_playlist)
            
        except KeyboardInterrupt:
            print("\nDownload cancelled by user")
            break
        except Exception as e:
            print(f"\nUnexpected error: {str(e)}")
            continue

if __name__ == "__main__":
    main()