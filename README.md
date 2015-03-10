# oscars-data-capitalone
Code that analyzes data from the 2015 Oscars.

Place oscar_tweets.csv in the `resources` folder.

## Setup
To run this project, you must have the following installations:

1. Python 2.7.5 or compatible version.
2. [Node.js](http://nodejs.org).
3. Bower (`npm install -g bower`)

## Usage
To analyze the csv file, cd into the `src` folder and run the `python analyze.py` command.

To view the web app, run the following commands in the project root:

1. `npm install`
2. `bower install`
3. `npm start`

Then go to `http://localhost:8080` in a browser.
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
