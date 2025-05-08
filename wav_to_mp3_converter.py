import os
from pydub import AudioSegment
import argparse

def convert_wav_to_mp3(input_folder):
    """
    Convert all WAV files in the specified folder to MP3 format.
    The output MP3 files will have the same name as the input WAV files.
    """
    # Check if input folder exists
    if not os.path.exists(input_folder):
        print(f"Error: Folder '{input_folder}' does not exist.")
        return

    # Get all WAV files in the folder
    wav_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.wav')]
    
    if not wav_files:
        print(f"No WAV files found in '{input_folder}'.")
        return

    print(f"Found {len(wav_files)} WAV files to convert.")

    # Convert each WAV file to MP3
    for wav_file in wav_files:
        try:
            # Construct full file paths
            wav_path = os.path.join(input_folder, wav_file)
            mp3_path = os.path.join(input_folder, os.path.splitext(wav_file)[0] + '.mp3')

            # Convert WAV to MP3
            print(f"Converting: {wav_file}")
            audio = AudioSegment.from_wav(wav_path)
            audio.export(mp3_path, format='mp3')
            print(f"Successfully converted: {wav_file} -> {os.path.basename(mp3_path)}")

        except Exception as e:
            print(f"Error converting {wav_file}: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Convert WAV files to MP3 format')
    parser.add_argument('input_folder', help='Folder containing WAV files to convert')
    args = parser.parse_args()

    convert_wav_to_mp3(args.input_folder)

if __name__ == '__main__':
    main() 