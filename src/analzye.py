import csv, json

def openResource(s):
    return open('../resources/' + s)

csvfile = openResource('oscar_tweets.csv')
headers = json.load(openResource('headers.json'))
best_picture = [line.rstrip('\n') for line in openResource('best_pictures.txt').readlines()]

with csvfile as f:
    reader = csv.DictReader(f)
    i = 0
    #for row in reader:
        # logic here
