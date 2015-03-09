import csv
import json

from datetime import datetime, timedelta
from collections import defaultdict

def openResource(s):
    return open('../resources/' + s)

def openOutput(s):
    return open('../out/' + s, 'w')

bestPicture = 'Birdman'

csvfile = openResource('oscar_tweets.csv')
best_pictures = [line.rstrip('\n') for line in openResource('best_pictures.txt').readlines()]
headers = json.load(openResource('headers.json'))
states = json.load(openResource('states.json'))

popularityFile = openOutput('pop.json')
timeFile = openOutput('time.json')
stateFile = openOutput('states.json')

nomineeCount = defaultdict(int)
timeCount = defaultdict(int)
stateCount = defaultdict(int)

with csvfile as f:
    reader = csv.DictReader(f)
    for row in reader:

        # find mentions of Best Picture nominees
        text = row[headers['text']].lower();
        for title in best_pictures:
            t = title.lower()
            if t in text or t.replace(' ', '') in text:
                nomineeCount[title] += 1

                # record hour and minute if title is 'Birdman'
                if title == bestPicture:
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

# print output to console
print 'The best picture nominees in order of popularity were:'
for idx, title in enumerate(popularityRank):
    print idx + 1, ':', title
print ''

print 'Birdman was mentioned most often at', birdmanAnnounceTime.strftime('%I:%M %p')
print ''

print 'The states in order of Oscars tweet activity were:'
for idx, state in enumerate(stateRank):
    print idx + 1, ':', states[state][1]

# print output to files for web app
try:
    json.dump(popularityRank, popularityFile)
    json.dump({"time": birdmanAnnounceTime.isoformat(' ')}, timeFile)
    json.dump(stateCount, stateFile)
finally:
    popularityFile.close()
    timeFile.close()
    stateFile.close()
