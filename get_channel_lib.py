import argparse
import pandas as pd
from pytubefix import YouTube, Channel

def get_tube_lib(name):
    '''This function takes a channel name and returns a pandas dataframe with the video id, title, description, and thumbnail url.'''

    # create lists for the video id and title columns
    ids = []
    titles = []
    view_counts = []
    desc = []
    thumbnail_url = []
    # dictionary for reference
    video_dict = {}

    c = Channel(f'https://www.youtube.com/@{name}')

    print(f'---------------------Getting video information for {}---------------------------------------------------')

    for video in c.videos:
        ids.append(video.video_id)
        titles.append(video.title)
        desc.append(video.description)
        thumbnail_url.append(video.thumbnail_url)
        video_dict[video.video_id] = video.title

    # build and return pandas df with ids and titles as the two columns
    df = pd.DataFrame({
        'Video ID': ids,
        'Title': titles,
        'Description': desc,
        'Thumbnails': thumbnail_url
    })

    return df, video_dict

def main():
    parser = argparse.ArgumentParser(description="Fetch video details from a YouTube channel.")
    parser.add_argument('channel_name', type=str, help='The name of the YouTube channel.')

    args = parser.parse_args()
    channel_name = args.channel_name

    df, video_dict = get_tube_lib(channel_name)
    df.to_csv(f'{channel_name}_videos.csv', index=False)
    print(df)

if __name__ == "__main__":
    main()
