import tweepy
import csv

consumer_key = "QmbhyDMaaOlUFb8RBTRTakVz1"
consumer_secret = "xs3w65GAF3RoY1FA0verJORitAVQB2H2v9oAE3r8nWcQXKuyY1"
callback_uri = "oob"

tweet_list = []


# Connect to the App
auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)
# Get authorization
redirect_url = auth.get_authorization_url()
print(redirect_url)

# user_pin_input = input("Enter the pin value: ")
# auth.get_access_token(str(user_pin_input))
# print(auth.access_token, auth.access_token_secret)

# Connect to the API, Tweepy
api = tweepy.API(auth, wait_on_rate_limit=True)

MAX_TWEETS = 10


# Open a ht.csv
with open('ht.csv', 'r') as csv_file:
    # read access
    csv_reader = csv.reader(csv_file)

    with open('ht.csv', 'w',) as file:
        # Write access
        writer = csv.writer(file)

        # Write the tweets into the csv files
        for tweet in tweepy.Cursor(api.search, q='#fmty', ).items(MAX_TWEETS):
            print(tweet.text, tweet.source_url)
            tweet_list.append([tweet.text, tweet.source_url])
            writer.writerow(["tweet", "source"])
            writer.writerows([tweet.text.encode('utf-8')])
