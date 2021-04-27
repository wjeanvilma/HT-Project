# HT-Project
# Webscraping using Tweepy

## Setting Up

Create a twitter developper account.
Make sure you are able to explain exactly what the project is about, you will be ask some questions when creating your app.

Create a project.
This will allow you to have the keys you need to webscrape. It will also be used for authentification, so Twitter knows who you are. You will undersatnd better later.

Make sure you have python and pycharm installed on you computer. 

You should have a github account for the project, so you can backup everything.

## Code to web Scrape
import tweepy
import csv

# Be sure to use your own keys
consumer_key = "**************************"
consumer_secret = "******************************************************"
callback_uri = "oob"

tweet_list = []

# Connect to the App, authentification
auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)

# Get authorization
redirect_url = auth.get_authorization_url()

# Connect to the API, Tweepy
api = tweepy.API(auth, wait_on_rate_limit=True)

# Set the max tweets
MAX_TWEETS = 100

# path where to save your folder, Make sure you use your own path
path = "/Users/newowner/PycharmProjects/WebScrape/"

# open or create a csv file
with open(path+'test.csv', 'w') as file:
    # Write access
    writer = csv.writer(file, delimiter=',')

    # write the header of the csv file
    writer.writerow(["USERNAME", "DATE CREATED", "TEXTS",  "FAVORITES COUNT", "RETWEETS COUNT", "SOURCE"])
    
    # Write each tweets into the csv files
    for tweet in tweepy.Cursor(api.search, q='#test', delimiter=",",).items(MAX_TWEETS):
        writer.writerow([tweet.user.screen_name, tweet.created_at, tweet.text.encode('utf-8'), tweet.favorite_count, tweet.retweet_count, tweet.source])




