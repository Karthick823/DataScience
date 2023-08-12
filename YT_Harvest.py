from googleapiclient.discovery import build
import googleapiclient.errors
import pandas as pd
import seaborn as sns
import numpy as np

api_key = 'AIzaSyDWnmLmdLV8qlQmsTIGlP12ckH3NzW6pGQ'
Channel_ids = [
    'UCpOnZdJQxa5vyR5dNtIoNjg',
    'UCgVsZwVGsBC74W4QW4o2LZQ',
    'UCCifgw5heieu3rESMxs_oRQ',
    'UCIUXCy7y_vMtRmvc0kc3c3w',
    'UCyEd6QBSgat5kkC6svyjudA'
    ]
youtube = build('youtube','v3', developerKey=api_key)

def channel_stats(youtube, Channel_ids):
    all_data = []
    request = youtube.channels().list(
        part = 'snippet,contentDetails,statistics',
        id = ','.join(Channel_ids)
    )
    response = request.execute()
    for i in range(len(response['items'])):
        data = dict(
            Channel_name =response['items'][i]['snippet']['title'],
            Subscribers = response['items'][i]['statistics']['subscriberCount'],
            Views = response['items'][i]['statistics']['viewCount'],
            videoCount = response['items'][i]['statistics']['videoCount'],
            Playlist_ID = response['items'][i]['contentDetails']['relatedPlaylists']['uploads']
            )
        
        all_data.append(data)
    
    return all_data
channel_stats(youtube, Channel_ids)