# oscars-data-capitalone
Code that analyzes data from the 2015 Oscars.

Place oscar_tweets.csv in the "resources" folder.

## Usage
This project was built with Python 2.7.5.
To run the web app, you must have [Node.js](http://nodejs.org) installed on your computer.

To analyze the csv file, cd into the "src" folder and run the "python analyze.py" command.

To view the web app, run "npm install", followed by "npm start", then go to "http://localhost:8080" in a browser.
You must have first run analyze.py for the web app to work correctly.

## Prompt
Using the dataset found here (https://s3.amazonaws.com/mindsumo/public/oscar_tweets.csv+(1).zip) and the programming language of your choice, submit the following:

1. Popularity Rank: A list of the most tweeted about best picture nominees (ranked from 1-8) 
2. Winner Announcement Prediction: Hour and minute when the winner (Birdman) was mentioned on Twitter most frequently 
3. Location: A list of which states were the most active in tweeting about #TheOscars2015 (rank ordered from most active to least)

Optional: 
Visualize the data trends. (e.g. Create a simple web or mobile app that displays the data points listed above and any other interesting trends you identify.)

Criteria: 
Your application will be judged on its efficiency, clarity, and style.
