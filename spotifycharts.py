import csv
import requests
from datetime import date, timedelta

#Available Spotify charts dates for files
sdate = date(2017, 1, 1)   # start date
edate = date(2019, 9, 25)   # end date
delta = edate - sdate       # days diff
allcharts = []

with requests.Session() as chartSession:
    for i in range(delta.days+1):
        day = (edate - timedelta(days=i))
        dayURL = day.strftime("%Y") + "-" +day.strftime("%m") + "-" + day.strftime("%d")
        download = chartSession.get('https://spotifycharts.com/regional/br/daily/' + dayURL + '/download')
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        counter = 1
        #Centralize all rows from all files into a single file
        for row in my_list: 
            if(counter>2): #not file header
                row.append(dayURL)
                allcharts.append(row)
            counter = counter + 1

with open("charts.csv", "w", newline='') as chartsCSV:
    wr = csv.writer(chartsCSV, quoting=csv.QUOTE_ALL)
    for row in allcharts:
        wr.writerow(row)

print(len(allcharts))