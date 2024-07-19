import argparse
import pandas as pd
from pytubefix import YouTube, Channel

<<<<<<< HEAD
def get_tube_lib(channel_names):
    '''This function takes a channel names and returns a pandas dataframe with the channel name, video id, video title, description, and thumbnail url.'''
    
=======
def get_tube_lib(name):
    '''This function takes a channel name and returns a pandas dataframe with the video id, title, description, and thumbnail url.'''

>>>>>>> ecb36bdd2595e516ca04b262fedbfdfaa2355b6f
    # create lists for the video id and title columns
    channels = []
    ids = []
    titles = []
    view_counts = []
    desc = []
    thumbnail_url = []
    # dictionary for reference
    video_dict = {}

<<<<<<< HEAD
    for name in channel_names:
=======
    c = Channel(f'https://www.youtube.com/@{name}')

    print(f'---------------------Getting video information for {}---------------------------------------------------')

    for video in c.videos:
        ids.append(video.video_id)
        titles.append(video.title)
        desc.append(video.description)
        thumbnail_url.append(video.thumbnail_url)
        video_dict[video.video_id] = video.title
>>>>>>> ecb36bdd2595e516ca04b262fedbfdfaa2355b6f

        print(f'Getting videos information for {name}')
    
        c = Channel(f'https://www.youtube.com/@{name}')
    
        for video in c.videos:
            print(f'Processing video information for {video.title}')
            channels.append(video.author)
            ids.append(video.video_id)
            titles.append(video.title)
            desc.append(video.description)
            thumbnail_url.append(video.thumbnail_url)
            video_dict[video.video_id] = video.title
    # build and return pandas df with ids and titles as the two columns
    df = pd.DataFrame({
            'Channel Name':channels,
            'Video ID': ids,
            'Title': titles,
            'Description': desc,
            'Thumbnails': thumbnail_url
    })

    return df, video_dict

def main():
    parser = argparse.ArgumentParser(description="Fetch video details from a YouTube channel.")
    parser.add_argument('channel_names', nargs='+', help='The names of the YouTube channels. i.e. Channel1 Channel2')

    args = parser.parse_args()
    channel_names = args.channel_names

    df, video_dict = get_tube_lib(channel_names)
    output_filename = '_'.join(channel_names) + '_videos.csv'
    df.to_csv(output_filename, index=False)
    print(df)

if __name__ == "__main__":
    main()
