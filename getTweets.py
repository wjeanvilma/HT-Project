
import tweepy
import csv

# Be sure to use your own keys
consumer_key = "QmbhyDMaaOlUFb8RBTRTakVz1"
consumer_secret = "xs3w65GAF3RoY1FA0verJORitAVQB2H2v9oAE3r8nWcQXKuyY1"
callback_uri = "oob"

tweet_list = []

# Connect to the App
auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)
# Get authorization
redirect_url = auth.get_authorization_url()
print(redirect_url)

# Connect to the API, Tweepy
api = tweepy.API(auth, wait_on_rate_limit=True)

MAX_TWEETS = 100

# path where to save your folder
path = "/Users/newowner/PycharmProjects/Email/"

# open or create a csv file
with open(path+'test.csv', 'w') as file:
    # Write access
    writer = csv.writer(file, delimiter=',')

    # write the header of the csv file
    writer.writerow(["USERNAME", "DATE CREATED", "TEXTS",  "FAVORITES COUNT", "RETWEETS COUNT", "SOURCE"])
    # Write the tweets into the csv files
    for tweet in tweepy.Cursor(api.search, q='#test', delimiter=",",).items(MAX_TWEETS):
        print(tweet.user.screen_name, tweet.created_at, tweet.text.encode('utf-8'), tweet.favorite_count, tweet.retweet_count, tweet.source)
        writer.writerow([tweet.user.screen_name, tweet.created_at, tweet.text.encode('utf-8'), tweet.favorite_count, tweet.retweet_count, tweet.source])

