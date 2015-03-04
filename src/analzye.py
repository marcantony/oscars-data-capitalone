import csv

file = '../resources/oscar_tweets.csv'

headers = {
    "time": "Time",
    "id": " ID",
    "text": " Text",
    "retweets": " Retweets",
    "geotag": " GeoTag",
    "placetag": " PlaceTag",
    "favorites": " Favorites",
    "name": " User Name",
    "loc": " User Location",
    "userid": " User ID",
    "timezone": " Time Zone",
    "followers": " User Followers",
    "statuses": " User Statuses",
    "friends": " User Friends",
    "handle": " User Handle",
    "hashtags": " HashTags in Tweet",
    "mentions": " UserMentions in Tweet"
}

best_picture = [
    "American Sniper",
    "Birdman",
    "Boyhood",
    "The Grand Budapest Hotel",
    "The Imitation Game",
    "Selma",
    "The Theory of Everything",
    "Whiplash"
]

with open(file) as f:
    reader = csv.DictReader(f)
    i = 0
    for row in reader:
        # logic here
