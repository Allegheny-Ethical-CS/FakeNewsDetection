import json
import os

import pandas as pd
from bluebird import BlueBird
from bluebird.scraper import BlueBird

from sentiment import PoliticalClassification
from train import TrainingML

col_names32 = "created_at,id,id_str,full_text,truncated,display_text_range,entities,source,in_reply_to_status_id,in_reply_to_status_id_str,in_reply_to_user_id,in_reply_to_user_id_str,in_reply_to_screen_name,user_id,user_id_str,geo,coordinates,place,contributors,is_quote_status,retweet_count,favorite_count,conversation_id,conversation_id_str,favorited,retweeted,possibly_sensitive,possibly_sensitive_editable,lang,supplemental_language,,self_thread"
# api = TwitterClient()
# trained_model = TrainingML()
# sentiment = PoliticalClassification()

user_results = "../data/results.csv"


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
        with open('../data/temp.json', 'w') as temp:
            json.dump(tweet, temp)
        df = pd.read_json('../data/temp.json', lines=True)
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
        with open('data/temp.json', 'w') as temp:
            json.dump(tweet, temp)
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
        with open('data/temp.json', 'w') as temp:
            json.dump(tweet, temp)
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
        os.remove('../results.csv')
        os.remove('../temp.csv')
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


if __name__ == '__main__':
    # calls main function
    main()
