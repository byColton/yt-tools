import pandas as pd
import os
from pytubefix import YouTube
import whisper
import argparse

def fetch_transcripts(file):
    df = pd.read_csv(file)
    df = df.head(3)
    
    for id_num in df['Video ID'].to_list():
        try:
            print(f'Transcripting {id_num}.')
            # Download the video audio
            yt = YouTube(f'https://youtube.com/watch?v={id_num}')
            audio = yt.streams.filter(only_audio=True).first()
            audio.download(output_path='.', filename=f'{id_num}.mp3')

            # Use Whisper to transcribe the audio
            model = whisper.load_model("base")
            result = model.transcribe(f'{id_num}.mp3')
            transcription_text = result['text']

            # Remove the audio file
            os.remove(f'{id_num}.mp3')

            # Save the transcription text to a .txt file
            with open(f'{id_num}.txt', 'w') as text_file:
                text_file.write(transcription_text)
            
            print(f"Transcription saved to {id_num}.txt")

        except Exception as e:
            print(f"Error processing video {id_num}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Fetch and transcribe YouTube videos.")
    parser.add_argument('file', type=str, help='The CSV file containing YouTube video IDs.')
    args = parser.parse_args()
    
    fetch_transcripts(args.file)
    print('Transcripts complete.')
if __name__ == "__main__":
    main()
