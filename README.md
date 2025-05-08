# Audio Manager

A comprehensive suite of Python tools for audio processing, transcription, and management.

## Features

- **Audio Track Separation**: Separate audio tracks into different stems (instruments) using Demucs
- **YouTube Audio Download**: Download audio from YouTube videos
- **Audio Transcription**: Transcribe audio files to text
- **WAV to MP3 Conversion**: Convert WAV files to MP3 format
- **Audio Extraction**: Extract audio from video files

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/audio-manager.git
cd audio-manager
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Audio Track Separation

The audio separator uses Demucs, a state-of-the-art audio source separation model from Facebook Research, to separate audio tracks into different stems (instruments).

Basic usage:
```bash
python audio_separator.py path/to/your/audio/file.mp3
```

Advanced usage with options:
```bash
python audio_separator.py path/to/your/audio/file.mp3 --output_dir custom_output_folder --model htdemucs_ft
```

#### Options

- `input_file`: Path to the input audio file (required)
- `--output_dir`: Directory to save separated tracks (default: 'separated_tracks')
- `--model`: Model to use for separation (choices: htdemucs, htdemucs_ft, mdx, mdx_extra, default: htdemucs)

#### Available Models

- `htdemucs`: Default model, separates into:
  - Drums
  - Bass
  - Other instruments
  - Vocals
- `htdemucs_ft`: Fine-tuned version of htdemucs, better for specific genres
- `mdx`: MDX model, good for general purpose separation
- `mdx_extra`: Enhanced version of MDX model with improved quality

#### Output Format

The script creates a directory (default: 'separated_tracks') containing the separated audio files. Each stem is saved as a separate WAV file with the following naming convention:
- `{track_name}_drums.wav`
- `{track_name}_bass.wav`
- `{track_name}_other.wav`
- `{track_name}_vocals.wav`

Example output structure:
```
separated_tracks/
└── my_song/
    ├── my_song_drums.wav
    ├── my_song_bass.wav
    ├── my_song_other.wav
    └── my_song_vocals.wav
```

### YouTube Audio Download

Download audio from YouTube videos:
```bash
python youtube_audio_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Audio Transcription

Transcribe audio files to text:
```bash
python transcribe_audio.py path/to/your/audio/file.mp3
```

### WAV to MP3 Conversion

Convert WAV files to MP3 format:
```bash
python wav_to_mp3_converter.py path/to/your/audio/file.wav
```

### Audio Extraction

Extract audio from video files:
```bash
python extract_audio.py path/to/your/video/file.mp4
```

## Project Structure

```
audio-manager/
├── audio/              # Directory for audio files
├── separated_tracks/   # Output directory for separated tracks
├── transcription/      # Directory for transcription files
├── video/             # Directory for video files
├── tex/               # Directory for text files
├── audio_separator.py
├── youtube_audio_downloader.py
├── transcribe_audio.py
├── wav_to_mp3_converter.py
├── extract_audio.py
├── requirements.txt
└── README.md
```

## Requirements

See `requirements.txt` for a complete list of dependencies.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 