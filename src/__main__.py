import re
import sys
from bluebird.scraper import BlueBird
import tweepy
from tweepy import OAuthHandler
from accessingTwitterData import TwitterClient
from train import TrainingML
from sentiment import PoliticalClassification
import matplotlib.pyplot as plt
from bluebird import BlueBird as bird


#api = TwitterClient()
#trained_model = TrainingML()
#sentiment = PoliticalClassification()

def main():
    print("Welcome to the Fake News Dection Program! \n")
    searching = input("Enter a term to search. \n")

    query = {
        'fields': [
            {'items': [searching]},
        ]
    }

    for tweet in BlueBird().stream(query):
        print(tweet)

    """
    print("Welcome to the Fake News Detection Program!\n")
    user = input("Twitter user to examine: \n")
    query = {
        'fields': [
            {'items': [str(user)]},
        ],
        'since': '2021-01-06',
        'until': '2021-01-07'
    }
    limit = 25
    index = 0
    while index <= 25:
        for tweet in BlueBird().search(query):
            with open('data/test.txt', 'a') as f:
                f.write(str(tweet)+"\n")
                f.close()
                index += 1
            if index == 25:
                exit()



# def main():
#     print("Welcome to the Fake News Detection Program!\n")
#     user = input("Twitter user to examine: \n")
#     # creating object of TwitterClient Class
#     # checking if user exists
#     user_id = api.search_for_user(screen_name = user)
#     # calling function to get tweets
#     tweets = api.get_user_tweets(user_id = user_id, count = 200)

#     model_choice = input("Which model suits you?\n0 = Naive Bayes\t1 = Linear SVM\n")
#     print("Collecting and labeling tweets...\n")

#     # appending user data to model for labeling
#     for tweet in tweets:
#         trained_model.predict_and_label(tweet, model_choice)
#     # set of only tweets marked political
#     political_tweets = [tweet for tweet in tweets if tweet['label'] == 'POLIT']
#     # get classification for each tweet in
#     for tweet in political_tweets:
#         tweet['classification'] = sentiment.get_tweet_sentiment(tweet['text'])

    else:
        print("Have a nice day :)")"""


if __name__ == '__main__':
    # calls main function
    main()

#Adapted from Zach Leonardo's senior comp project.
#Linked here: https://github.com/leonardoz15/Polarized
