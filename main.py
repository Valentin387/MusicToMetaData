import os
import json
from mutagen.mp3 import MP3
from mutagen.id3 import ID3TimeStamp

def convert_to_json_serializable(value):
    # Convert ID3TimeStamp objects to string
    if isinstance(value, ID3TimeStamp):
        return str(value)
    return value

def extract_metadata(file_path):
    try:
        audio = MP3(file_path)
        metadata = {
            #'name': os.path.basename(file_path),
            'title': audio.tags.get('TIT2', [''])[0],
            'subtitle': audio.tags.get('TIT3', [''])[0],
            'bitrate': int(audio.info.bitrate / 1000),  # Convert to kbps
            'commentaries': audio.tags.get('COMM', [''])[0],
            'main_artist': audio.tags.get('TPE1', [''])[0],
            'collaborators': audio.tags.get('TPE2', [''])[0],
            'album_artist': audio.tags.get('TPE4', [''])[0],
            'album': audio.tags.get('TALB', [''])[0],
            'year': audio.tags.get('TDRC', [''])[0],
            'track_number': audio.tags.get('TRCK', [''])[0],
            'genre': audio.tags.get('TCON', [''])[0],
            'duration': int(audio.info.length)  # Duration in seconds
        }
        # Convert values to JSON serializable format
        metadata = {key: convert_to_json_serializable(value) for key, value in metadata.items()}
        return metadata
    except Exception as e:
        print(f"Error extracting metadata from {file_path}: {str(e)}")
        return None

def main():
    folder_path = r"C:/Users/valentin/Music/workout 02"  # Replace with the path to your folder
    all_metadata = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.mp3'):
            file_path = os.path.join(folder_path, file_name)
            metadata = extract_metadata(file_path)
            if metadata:
                all_metadata.append(metadata)

    # Write all metadata to a JSON file
    with open('metadata.json', 'w') as json_file:
        json.dump(all_metadata, json_file, indent=4)

    print("Metadata exported to metadata.json")

if __name__ == "__main__":
    main()
