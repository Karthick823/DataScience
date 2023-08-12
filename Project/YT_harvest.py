from googleapiclient.discovery import build
import pandas as pd
import seaborn as sns

api_key = 'AIzaSyDWnmLmdLV8qlQmsTIGlP12ckH3NzW6pGQ'
Channel_ids = ['UCpOnZdJQxa5vyR5dNtIoNjg',
              'UCgVsZwVGsBC74W4QW4o2LZQ',
              'UCCifgw5heieu3rESMxs_oRQ',
              'UCIUXCy7y_vMtRmvc0kc3c3w',
              'UCyEd6QBSgat5kkC6svyjudA'
              ]
youtube = build('youtube','v3',developerKey=api_key)

def channel_stats(youtube, Channel_ids):
    response = youtube.channels().list(
        part = 'snippet,contentDetails,statistics',
        id = ','.join(Channel_ids)
    )
    response = request.execute()
    
    return response
#channel_stats(youtube,Channel_ids)