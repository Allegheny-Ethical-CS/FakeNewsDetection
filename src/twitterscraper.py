
import os

import pandas as pd
from bluebird import BlueBird
from io import StringIO
import streamlit as st


class Twitter(object):

    def __init__(self):
        self.col_names32 = StringIO("""created_at,id,id_str,full_text,truncated,display_text_range,entities,source,in_reply_to_status_id,in_reply_to_status_id_str,in_reply_to_user_id,in_reply_to_user_id_str,in_reply_to_screen_name,user_id,user_id_str,geo,coordinates,place,contributors,is_quote_status,retweet_count,favorite_count,conversation_id,conversation_id_str,favorited,retweeted,possibly_sensitive,possibly_sensitive_editable,lang,supplemental_lang,,self_thread""")
    #api = TwitterClient()
    #trained_model = TrainingML()
    #sentiment = PoliticalClassification()
        self.bird = BlueBird()
        self.user_results = "./data/results.csv"
        self.max = 5

    def search_term(self, searching):
        progressbar = st.progress(0)
        index = 0
        query = {
            'fields': [
                {'items': [searching]},
            ]
        }
        results_df = pd.DataFrame(
            columns=['index', 'created_at', 'full_text', 'user_id'])
        for tweet in self.bird.search(query):

            index += 1
            user = self.bird.get_user_by_id(str(tweet['user_id']))
            res = {"created_at": tweet['created_at'],
                   "full_text": tweet['full_text'], "user_id": user['screen_name']}
            results_df = results_df.append(res, ignore_index=True)
            if index ==self.max:
                return results_df
            else:
                progressbar.progress(index/self.max)

    def search_hashtag(self, searching):
        progressbar = st.progress(0)
        index = 0
        query = {
            'fields': [
                {'items': [searching], 'target':'hashtag'},
            ]
        }
        results_df = pd.DataFrame(
            columns=['index', 'created_at', 'full_text', 'user_id'])
        for tweet in self.bird.search(query):

            index += 1
            user = self.bird.get_user_by_id(str(tweet['user_id']))
            res = {"created_at": tweet['created_at'],
                "full_text": tweet['full_text'], "user_id": user['screen_name']}
            results_df = results_df.append(res, ignore_index=True)
            if index ==self.max:
                return results_df
            else:
                progressbar.progress(index/self.max)

    def search_user(self, searching):
        progressbar = st.progress(0)
        index = 0
        query = {
            'fields': [
                {'items': [searching], 'target':'from'},
            ]
        }
        results_df = pd.DataFrame(
            columns=['index', 'created_at', 'full_text', 'user_id'])
        for tweet in self.bird.search(query):
            
            index += 1
            user = self.bird.get_user_by_id(str(tweet['user_id']))
            res = {"created_at": tweet['created_at'],
                   "full_text": tweet['full_text'], "user_id": user['screen_name']}
            results_df = results_df.append(res, ignore_index=True)
            print("Found tweet", index, "out of 50")
            if index ==self.max:
                return results_df
            else:
                progressbar.progress(index/self.max)
