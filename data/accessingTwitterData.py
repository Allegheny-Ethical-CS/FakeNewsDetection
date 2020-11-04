import os
import tweepy as tw
import pandas as pd

def accessingTwitterDataMethod(): 
    #login credentials for Twitter
    #will be changing this from my personal account later; I will need a developer account
    consumer_key = `Rachael19014996`
    consumer_secret = `mozilla1234`
    access_token = `Rachael19014996`
    access_token_secret = `mozilla1234`

    #Logging in to Twitter with login credentials
    auth.tw = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit = True)

    #Searching for relevant Tweets
    search_words = "Presidential Election"
    date_since = "2020-10-27" #Twitter API only allows you to access the past few weeks of Tweets, so we will start pretty recently

    #Collecting Tweets
    tweets = tw.Cursor(api.search, q = search_words, lang = "en", since=date_since).items(50)
    #items(50) is going to return 50 of the most recent Tweets. This will allow us to create a smaller data pool

    <tweepy.cursor.ItemIterator at 0x7fafc296e400>
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

    #adapted from Earth Data Science
    #Link: https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/twitter-data-in-python/
    return tweets