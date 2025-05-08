import speech_recognition as sr
from pydub import AudioSegment
import os
import sys
import tempfile

def convert_to_wav(audio_path):
    """Convert audio file to WAV format if it's not already WAV."""
    if audio_path.lower().endswith('.wav'):
        return audio_path
    
    # Create a temporary file for the WAV conversion
    temp_wav = tempfile.NamedTemporaryFile(suffix='.wav', delete=False)
    temp_wav.close()
    
    # Convert to WAV
    audio = AudioSegment.from_file(audio_path)
    audio.export(temp_wav.name, format='wav')
    return temp_wav.name

def transcribe_audio(audio_path, output_path=None):
    try:
        # Check if input file exists
        if not os.path.exists(audio_path):
            print(f"Error: Input file '{audio_path}' does not exist.")
            return False

        # Set default output path if none provided
        if output_path is None:
            output_path = os.path.splitext(audio_path)[0] + '.txt'
        
        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(output_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        print(f"Transcribing audio from: {audio_path}")
        
        # Convert audio to WAV if necessary
        wav_path = convert_to_wav(audio_path)
        
        # Initialize recognizer
        recognizer = sr.Recognizer()
        
        # Open the audio file
        with sr.AudioFile(wav_path) as source:
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source)
            
            # Record the audio
            audio_data = recognizer.record(source)
            
            print("Transcribing... This may take a few minutes.")
            
            # Perform speech recognition
            text = recognizer.recognize_google(audio_data, language='es-ES')
            
            # Write the transcription to file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(text)
            
            print(f"Successfully transcribed audio to: {output_path}")
            
            # Clean up temporary WAV file if it was created
            if wav_path != audio_path:
                os.unlink(wav_path)
            
            return True
            
    except sr.UnknownValueError:
        print("Error: Speech recognition could not understand the audio")
        return False
    except sr.RequestError as e:
        print(f"Error: Could not request results from speech recognition service; {str(e)}")
        return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("\nTroubleshooting tips:")
        print("1. Make sure the audio file is not corrupted")
        print("2. Check your internet connection (required for Google's speech recognition)")
        print("3. Verify that the audio file has clear speech")
        print("4. Make sure the audio is in Spanish")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python transcribe_audio.py <audio_file> [output_file.txt]")
        print("\nExample:")
        print("python transcribe_audio.py audio.mp3")
        print("python transcribe_audio.py audio.mp3 transcription.txt")
        return
    
    audio_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    transcribe_audio(audio_path, output_path)

if __name__ == "__main__":
    main() 