from pytube import YouTube
import os
import sys
import re

def is_valid_youtube_url(url):
    # Regular expression for YouTube URL validation
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    
    youtube_regex_match = re.match(youtube_regex, url)
    return bool(youtube_regex_match)

def download_audio(url, output_path=None):
    try:
        # Validate URL
        if not is_valid_youtube_url(url):
            print("Error: Invalid YouTube URL. Please provide a valid YouTube video URL.")
            return False

        # Create YouTube object with retry mechanism
        max_retries = 3
        for attempt in range(max_retries):
            try:
                yt = YouTube(url)
                # Test if we can access the video info
                _ = yt.title
                break
            except Exception as e:
                if attempt == max_retries - 1:
                    raise e
                print(f"Attempt {attempt + 1} failed, retrying...")
                continue
        
        # Get the audio stream
        audio_stream = yt.streams.filter(only_audio=True).first()
        
        if not audio_stream:
            print("No audio stream found for this video.")
            return False
        
        # Set default output path if none provided
        if output_path is None:
            output_path = os.path.join(os.getcwd(), "downloads")
        
        # Create output directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)
        
        # Download the audio
        print(f"Downloading: {yt.title}")
        audio_file = audio_stream.download(output_path=output_path)
        
        # Rename the file to .mp3
        base, _ = os.path.splitext(audio_file)
        new_file = base + '.mp3'
        os.rename(audio_file, new_file)
        
        print(f"Successfully downloaded to: {new_file}")
        return True
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("\nTroubleshooting tips:")
        print("1. Make sure the video is not age-restricted or private")
        print("2. Check your internet connection")
        print("3. Verify that the URL is correct and the video exists")
        print("4. Try using a different YouTube video URL")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python youtube_audio_downloader.py <youtube_url> [output_path]")
        print("\nExample:")
        print("python youtube_audio_downloader.py https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        return
    
    url = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    download_audio(url, output_path)

if __name__ == "__main__":
    main() 