"""Class to return tweets of given parameters from twitter in dataframe."""

from io import StringIO
import pandas as pd
from bluebird import BlueBird
from io import StringIO
import streamlit as st


class Twitter():
    """Return tweets of given parameters from twitter in dataframe."""

    def __init__(self):
        self.bird = BlueBird()
        self.user_results = "./data/results.csv"
        self.max = 5

    def search_term(self, searching):
        """Utility function to return given number of tweets with search term in body."""

        progressbar = st.progress(0)
        index = 0
        query = {
            'fields': [
                {'items': [searching]},
            ]
        }

        results_df = pd.DataFrame(
            columns=['index', 'created_at', 'full_text', 'user_id'])
        for tweet in BlueBird().search(query):

            index += 1
            user = BlueBird().get_user_by_id(str(tweet['user_id']))
            res = {
                "created_at": tweet['created_at'],
                "full_text": tweet['full_text'],
                "user_id": user['screen_name']
            }

            results_df = results_df.append(res, ignore_index=True)
            if index ==self.max:
                return results_df
            else:
                progressbar.progress(index/self.max)


    def search_hashtag(self, searching):
        """Utility function to return given number of tweets with given
        hashtag."""

        progressbar = st.progress(0)
        index = 0
        query = {
            'fields': [
                {'items': [searching], 'target': 'hashtag'},
            ]
        }
        results_df = pd.DataFrame(
            columns=['index', 'created_at', 'full_text', 'user_id'])
        for tweet in BlueBird().search(query):

            index += 1
            user = BlueBird().get_user_by_id(str(tweet['user_id']))
            res = {
                "created_at": tweet['created_at'],
                "full_text": tweet['full_text'],
                "user_id": user['screen_name']
            }

            results_df = results_df.append(res, ignore_index=True)
            if index ==self.max:
                return results_df
            else:
                progressbar.progress(index/self.max)

    def search_user(self, searching):
        """Utility function to return given number of tweets with given
        username as creator or tagged."""

        progressbar = st.progress(0)
        index = 0
        query = {
            'fields': [
                {'items': [searching], 'target': 'from'},
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
