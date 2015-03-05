import csv
import json

from datetime import datetime
from collections import defaultdict

def openResource(s):
    return open('../resources/' + s)

csvfile = openResource('oscar_tweets.csv')
headers = json.load(openResource('headers.json'))
best_pictures = [line.rstrip('\n') for line in openResource('best_pictures.txt').readlines()]

with csvfile as f:
    reader = csv.DictReader(f)
    nomineeCount = defaultdict(int)
    timeCount = defaultdict(int)
    popularityRank = list()
    for row in reader:

        # find mentions of Best Picture nominees
        text = row[headers['text']].lower();
        for title in best_pictures:
            t = title.lower()
            if t in text or t.replace(' ', '') in text:
                nomineeCount[title] += 1

                # record hour and minute if title is 'Birdman'
                if title == 'Birdman':
                    mention_time = datetime.strptime(row[headers['time']],
                        '%a %b %d %H:%M:%S +0000 %Y').replace(second=0)
                    timeCount[mention_time] += 1

    popularityRank = sorted(nomineeCount, key=nomineeCount.get, reverse=True)
    birdmanAnnounceTime = max(timeCount, key=timeCount.get)
   
    print birdmanAnnounceTime.strftime('%H:%M %p')
    print popularityRank
