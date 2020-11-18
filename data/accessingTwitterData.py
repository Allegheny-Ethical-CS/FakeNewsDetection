import os
import tweepy as tw #install tweepy in terminal
from tweepy import OAuthHandler
#import pandas as pd

def accessingTwitterDataMethod(): 
    #login credentials for Twitter
    consumer_key = '9YBmnvZTfFIh79rg5VKSNpOWP'
    consumer_secret = 'iYOo4HSo46EkdmrJuzRyxg5iJK517X6zYSIZezx0pIfc5I3CyN'
    access_token = '1324034835397169155-7LIFJavLSJCREPGx94PzI3ExWTHpgH'
    access_token_secret = 'GITr1dMvmLuVxLJhBDwW2icobojbZl6K9WT71eE3ts4zq'

    #username: Rachael19014996
    #password: mozilla1234

    #API key
    # 9YBmnvZTfFIh79rg5VKSNpOWP

    #API secret key
    # iYOo4HSo46EkdmrJuzRyxg5iJK517X6zYSIZezx0pIfc5I3CyN
    
    #Bearer token
    # AAAAAAAAAAAAAAAAAAAAAICYJgEAAAAAArrADqBYNgp5oetqwRXrxa%2BhRoI%3D94xDChGBzDsZGXP1C80T45acUjfHTxe0zjAwQurZThwQFBtly3


    #Access token
    #1324034835397169155-7LIFJavLSJCREPGx94PzI3ExWTHpgH

    #Access token secret
    #GITr1dMvmLuVxLJhBDwW2icobojbZl6K9WT71eE3ts4zq

    #https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens
    #https://github.com/leonardoz15/Polarized/blob/master/src/twitter.py

    #Logging in to Twitter with login credentials
    auth.tw = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit = True)

    
    #try:
        #self.auth = OAuthHandler(consumer_key, consumer_secret)
        #set access token and secret
        #self.auth.set_access_token(access_token, access_token_secret)
        #create twitter api object to fetch tweets
        #self.api = tweepy.API(self.auth)
    #except:
        #print("Error: Authentication Failed")

    #Searching for relevant Tweets
    search_words = "#Election"
    date_since = "2020-11-17" #Twitter API only allows you to access the past few weeks of Tweets, so we will start pretty recently

    #Collecting Tweets
    tweets = tw.Cursor(api.search, q = search_words, lang = "en", since=date_since).items(50)
    #items(50) is going to return 50 of the most recent Tweets. This will allow us to create a smaller data pool
    print(tweets)

    #<tweepy.Cursor.ItemIterator at 0x7fafc296e400>
    #.Cursor() returns an object that can be iterated or looped through to access the data collected
    #The data that has been collected that we will use is the text of the Tweet, who sent the Tweet, and the date the Tweet was sent.
    #With the text of the tweet, we will be able to most clearly detect "fake news", but an additional level will come from who sent the Tweet. 
    #In this sense, we will be checking to see if the author is verified on Twitter or not.

    #Filter out the retweets
    new_search = search_words + " -filter:retweets"
    tweets = tw.Cursor(api.search, q = new_search, lang = "en", since = date_since).items(50)

    #Print Tweets in list form.
    [tweet.text for tweet in tweets]
    user_data = [[tweet.user.screen_name] for tweet in tweets]
    #Get the username of the Tweet author
    print(tweets)

    #adapted from Earth Data Science
    #Link: https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/twitter-data-in-python/
    return tweets