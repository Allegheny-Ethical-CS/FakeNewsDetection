import json
import os

import pandas as pd
from bluebird import BlueBird
from bluebird.scraper import BlueBird

from sentiment import PoliticalClassification
from train import TrainingML

col_names32 = "created_at,id,id_str,full_text,truncated,display_text_range,entities,source,in_reply_to_status_id,in_reply_to_status_id_str,in_reply_to_user_id,in_reply_to_user_id_str,in_reply_to_screen_name,user_id,user_id_str,geo,coordinates,place,contributors,is_quote_status,retweet_count,favorite_count,conversation_id,conversation_id_str,favorited,retweeted,possibly_sensitive,possibly_sensitive_editable,lang,supplemental_language,,self_thread"
#api = TwitterClient()
#trained_model = TrainingML()
#sentiment = PoliticalClassification()

user_results = "data/results.csv"


def search_term():
    index = 0
    searching = input("Enter a term to search. \n")

    query = {
        'fields': [
            {'items': [searching]},
        ]
    }
    for tweet in BlueBird().search(query):
        index += 1
        with open('data/temp.json', 'w') as l:
            json.dump(tweet, l)
        df = pd.read_json('data/temp.json', lines=True)
        with open(user_results, 'a') as f:
            df.to_csv(f, header=None, index=False)
        if index == 50:
            dummy_file = user_results + '.bak'
            with open(user_results, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
                write_obj.write(col_names32 + '\n')
                for line in read_obj:
                    write_obj.write(line)
            os.remove(user_results)
            os.rename(dummy_file, user_results)
            break


def search_hashtag():
    index = 0
    searching = input("Enter a hashtag to search. \n")

    query = {
        'fields': [
            {'items': [searching], 'target':'hashtag'},
        ]
    }
    for tweet in BlueBird().search(query):
        index += 1
        with open('data/temp.json', 'w') as l:
            json.dump(tweet, l)
        df = pd.read_json('data/temp.json', lines=True)
        with open(user_results, 'a') as f:
            df.to_csv(f, header=None, index=False)
        if index == 50:
            dummy_file = user_results + '.bak'
            with open(user_results, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
                write_obj.write(col_names32 + '\n')
                for line in read_obj:
                    write_obj.write(line)
            os.remove(user_results)
            os.rename(dummy_file, user_results)
            break


def search_user():
    index = 0
    searching = input("Enter a user to search. \n")

    query = {
        'fields': [
            {'items': [searching], 'target':'from'},
        ]
    }
    for tweet in BlueBird().search(query):
        index += 1
        with open('data/temp.json', 'w') as l:
            json.dump(tweet, l)
        df = pd.read_json('data/temp.json', lines=True)
        with open(user_results, 'a') as f:
            df.to_csv(f, header=None, index=False)
        if index == 50:
            dummy_file = user_results + '.bak'
            with open(user_results, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
                write_obj.write(col_names32 + '\n')
                for line in read_obj:
                    write_obj.write(line)
            os.remove(user_results)
            os.rename(dummy_file, user_results)
            break


def main():
    try:
        os.remove('data/results.csv')
        os.remove('data/temp.csv')
    except:
        print()
    print("Welcome to the Fake News Dection Program! \n")
    print("Would you like to search by:\nkeyword\nhashtag\nuser")
    done = False
    while done == False:
        choice = input("keyword/hashtag/user: ")
        if choice == "keyword":
            search_term()
            done = True
        elif choice == "hashtag":
            search_hashtag()
            done = True
        elif choice == "user":
            search_user()
            done = True
        else:
            print("Sorry, Bad Input. Please Enter One of the Options Below")
            done = False
    try:
        os.remove('data/temp.json')
    except:
        print()

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

# Adapted from Zach Leonardo's senior comp project.
# Linked here: https://github.com/leonardoz15/Polarized
