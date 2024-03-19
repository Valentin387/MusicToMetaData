# MP3 Metadata Extractor

This Python script extracts metadata from MP3 files and saves it to a JSON file. It can be useful for organizing and managing music libraries by collecting metadata such as title, artist, album, etc.

## Features

- Extracts metadata from MP3 files including:
  - Title
  - Subtitle
  - Bitrate
  - Commentaries
  - Main artist
  - Collaborators
  - Album artist
  - Album
  - Year
  - Track number
  - Genre
  - Duration

## Usage

1. Clone the repository or download the script `mp3_metadata_reader.py`.
2. Make sure you have Python installed on your system.
3. Install the required dependencies by running `pip install mutagen`.
4. Edit the `folder_path` variable in the script to specify the directory containing your MP3 files.
5. Run the script by executing `python mp3_metadata_reader.py` in your terminal or command prompt.
6. The script will extract metadata from all MP3 files in the specified directory and save it to a JSON file named `metadata.json`.

## Requirements

- Python 3.x
- `mutagen` library

## Example

Suppose you have a folder named `Music` containing several MP3 files. After running the script, a file named `metadata.json` will be created in the same directory as the script. This file will contain metadata for each MP3 file in the `Music` folder.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

