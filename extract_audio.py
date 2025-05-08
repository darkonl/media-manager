from moviepy.editor import VideoFileClip
import os
import sys

def extract_audio(video_path, output_path=None):
    try:
        # Check if input file exists
        if not os.path.exists(video_path):
            print(f"Error: Input file '{video_path}' does not exist.")
            return False

        # Check if input file is an MP4
        if not video_path.lower().endswith('.mp4'):
            print("Error: Input file must be an MP4 file.")
            return False

        # Set default output path if none provided
        if output_path is None:
            # Create output filename by replacing .mp4 with .mp3
            output_path = os.path.splitext(video_path)[0] + '.mp3'
        
        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(output_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        print(f"Extracting audio from: {video_path}")
        
        # Load the video file
        video = VideoFileClip(video_path)
        
        # Extract the audio
        audio = video.audio
        
        # Write the audio to file
        audio.write_audiofile(output_path)
        
        # Close the video and audio objects
        audio.close()
        video.close()
        
        print(f"Successfully extracted audio to: {output_path}")
        return True
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("\nTroubleshooting tips:")
        print("1. Make sure the video file is not corrupted")
        print("2. Check if you have enough disk space")
        print("3. Verify that the video file has an audio track")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python extract_audio.py <video_file.mp4> [output_file.mp3]")
        print("\nExample:")
        print("python extract_audio.py video.mp4")
        print("python extract_audio.py video.mp4 output.mp3")
        return
    
    video_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    extract_audio(video_path, output_path)

if __name__ == "__main__":
    main() 