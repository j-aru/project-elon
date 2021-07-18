#Twitter Scraper module
import tweepy
from tweepy import OAuthHandler

#http client for sentiment analysis API
import http.client, json

#importing necessary modules- datetime,count,time,re
from datetime import datetime, date
from itertools import count
import time
import re

# Store Twitter credentials from dev account
consumer_key = "A"
consumer_secret = "B"
access_key = "C-D"
access_secret = "E"
bearer_token="F%G"

# Pass twitter credentials to tweepy via its OAuthHandler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#crypto sign and keywords
keywords =['Bitcoin', 'bitcoin', 'BITCOIN', 'btc', 'BTC',"fucked","a","the","tesla","today","crypto","cryptocuurency"]
def get_elons_tweet():
    #Get Elon's last tweet by user ID
    tweets = tweepy.Cursor(api.user_timeline,id="44196397", since=date.today(), tweet_mode='extended').items(1)
    #remove all invalid characters
    elons_last_tweet = [re.sub('[^A-Za-z0-9]+', ' ', tweet.full_text) for tweet in tweets]
    #re-try until it returns a value - tweepy API fails to return the tweet sometimes
    while not elons_last_tweet:
        tweets = tweepy.Cursor(api.user_timeline,id="44196397", since=date.today(), tweet_mode='extended').items(1)
        elons_last_tweet = [re.sub('[^A-Za-z0-9]+', ' ', tweet.full_text) for tweet in tweets]
    return elons_last_tweet[0]


#what_musk_said contains the last tweet and the logic will check whether any of the keywords defined in our keywords variable above are present in Elon’s tweet. 
# If that is true,Check if Musk mentioned bitcoin with positive sentiment and print accordingly
def advice():
    from textblob import TextBlob
    what_musk_said = get_elons_tweet()
    sentiment=TextBlob(what_musk_said).sentiment[0]
    if any(keyword in what_musk_said for keyword in keywords) and sentiment>0:
       print(f'Buy crypto, price gonna surge')
    elif any(keyword in what_musk_said for keyword in keywords) and sentiment<0:
        print(f'Price dip ahead!')
    else:
        print("No new updates")





if __name__ == '__main__':
    print('Press Ctrl-C / Ctrl-Q to stop.')
    for i in count():
        print(f'Update {i}')
        advice()
        time.sleep(1)
