import csv
import json

from datetime import datetime, timedelta
from collections import defaultdict

def openResource(s):
    return open('../resources/' + s)

csvfile = openResource('oscar_tweets.csv')
headers = json.load(openResource('headers.json'))
best_pictures = [line.rstrip('\n') for line in openResource('best_pictures.txt').readlines()]
states = json.load(openResource('states.json'))

with csvfile as f:
    reader = csv.DictReader(f)
    nomineeCount = defaultdict(int)
    timeCount = defaultdict(int)
    stateCount = defaultdict(int)
    popularityRank = list()
    stateRank = list()
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

        # determine what state tweet is from, if data is available
        location = row[headers['loc']]
        for stateCode, stateNames in states.iteritems():
            try:
                if any(stateName in location for stateName in stateNames):
                    stateCount[stateCode] += 1
            except UnicodeDecodeError:
                continue

    popularityRank = sorted(nomineeCount, key=nomineeCount.get, reverse=True)
    birdmanAnnounceTime = max(timeCount, key=timeCount.get)
    stateRank = sorted(stateCount, key=stateCount.get, reverse=True)

    # naively convert to PST
    birdmanAnnounceTime += timedelta(hours=-8)
   
    print birdmanAnnounceTime.strftime('%I:%M %p')
    print popularityRank
    print json.dumps(stateCount)
    print stateRank
