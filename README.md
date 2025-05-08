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

Separate audio tracks into different stems (instruments):
```bash
python audio_separator.py path/to/your/audio/file.mp3
```

Options:
- `--output_dir`: Directory to save separated tracks (default: 'separated_tracks')
- `--model`: Model to use for separation (choices: htdemucs, htdemucs_ft, mdx, mdx_extra)

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