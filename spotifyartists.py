import csv
import requests
import json
import ndjson
from datetime import date, timedelta


#Spotify user token to retrieve data
myToken = '[userToken]'
#API endpoint
spotifyAPISearchURL = "https://api.spotify.com/v1/search?q="
#Spotify uses bearer token
head = {'Authorization': 'Bearer ' + myToken}

artistdata = []
relatedartist = []
#uniquecharts contains a filtered list of artists to be retrieved from the API. The original list is based on Spotify charts
with open('data/uniqueartistscharts.csv', 'r') as f:
    reader = csv.reader(f)
    allcharts = list(reader)
    i = 0
    for row in allcharts:
        i = i + 1
        if (i<10000):
            print(row[0])
            artist = row[0].replace(' ','%20') + "&type=artist"
            response = requests.get(spotifyAPISearchURL + artist, headers=head)
            artistdata.append(json.loads(response.content))
#Data are stored in ndjson format, a format supported by BigQuery import
with open('data/artistdata.ndjson', 'w', encoding='utf-8') as artistsFile:
    ndjson.dump(artistdata, artistsFile)
    
