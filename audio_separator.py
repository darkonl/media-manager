import os
import argparse
import torch
import torchaudio
import numpy as np
from demucs.pretrained import get_model
from demucs.apply import apply_model
from demucs.audio import AudioFile

def separate_audio(input_file, output_dir, model_name="htdemucs"):
    """
    Separate audio file into different stems (instruments)
    
    Args:
        input_file (str): Path to input audio file
        output_dir (str): Directory to save separated tracks
        model_name (str): Name of the model to use (default: htdemucs)
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Load the model
    model = get_model(model_name)
    model.cpu()
    model.eval()
    
    # Load the audio file
    wav = AudioFile(input_file).read(streams=0, samplerate=model.samplerate, channels=model.audio_channels)
    ref = wav.mean(0)
    wav = (wav - ref.mean()) / ref.std()
    
    # Perform the separation
    with torch.no_grad():
        sources = apply_model(model, wav[None])[0]
        sources = sources * ref.std() + ref.mean()
    
    # Save the separated tracks
    track_name = os.path.splitext(os.path.basename(input_file))[0]
    for source, name in zip(sources, model.sources):
        output_path = os.path.join(output_dir, f"{track_name}_{name}.wav")
        # Ensure the audio data is in the correct shape (channels, time)
        if len(source.shape) == 1:
            source = source.unsqueeze(0)  # Add channel dimension
        elif len(source.shape) > 2:
            source = source.squeeze()  # Remove extra dimensions
            if len(source.shape) == 1:
                source = source.unsqueeze(0)  # Add channel dimension back
        # Save using torchaudio
        torchaudio.save(
            output_path,
            source,  # Should be (channels, time)
            model.samplerate,
            format="wav"
        )
    
    print(f"Separation complete! Files saved in {output_dir}")

def main():
    parser = argparse.ArgumentParser(description='Separate audio file into different stems')
    parser.add_argument('input_file', help='Path to input audio file')
    parser.add_argument('--output_dir', default='separated_tracks',
                      help='Directory to save separated tracks (default: separated_tracks)')
    parser.add_argument('--model', default='htdemucs',
                      choices=['htdemucs', 'htdemucs_ft', 'mdx', 'mdx_extra'],
                      help='Model to use for separation (default: htdemucs)')
    
    args = parser.parse_args()
    
    separate_audio(args.input_file, args.output_dir, args.model)

if __name__ == '__main__':
    main()