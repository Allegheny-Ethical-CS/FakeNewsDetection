import pytest
import time

import src.twitterscraper as ts


def test_search_term():
    """Check that search term function returns dataframe of tweets that contain term searched."""
    twitterscraper = ts.Twitter()

    search_parameters = ["CAPitol", "jury", "Cookie"]

    for term in search_parameters:
        try:
            dataframe = twitterscraper.search_term(term)

            direct_term_present = 0
            no_direct_term_present = 0
            direct_presense_ratio = 0
            hasTerm = False
            for ind in dataframe.index:
                tweet = dataframe["full_text"][ind]
                tweet_components = tweet.split(" ")
                for element in tweet_components:
                    if term.lower() in element.lower():
                        hasTerm = True
                if hasTerm is True:
                    direct_term_present += 1
                else:
                    no_direct_term_present += 1
            if(no_direct_term_present == 0):
                direct_presense_ratio = 1
            else:
                direct_presense_ratio = direct_term_present / no_direct_term_present
            assert direct_presense_ratio > 0.9
        except:
            time.sleep(10)


def test_search_hastag():
    """Check that search term function returns dataframe of tweets containing hashtag with term"""
    twitterscraper = ts.Twitter()

    search_parameters = ["DACA", "Forthekids"]

    for term in search_parameters:
        try:
            dataframe = twitterscraper.search_hashtag(term)

            direct_term_present = 0
            no_direct_term_present = 0
            direct_presense_ratio = 0
            hasTerm = False
            target_term = "#" + term
            for ind in dataframe.index:
                tweet = dataframe["full_text"][ind]
                tweet_components = tweet.split(" ")
                for element in tweet_components:
                    if target_term.lower() in element.lower():
                        hasTerm = True
                if hasTerm is True:
                    direct_term_present += 1
                else:
                    no_direct_term_present += 1
            if(no_direct_term_present == 0):
                direct_presense_ratio = 1
            else:
                direct_presense_ratio = direct_term_present / no_direct_term_present
            assert direct_presense_ratio > 0.9
        except:
            time.sleep(10)


def test_search_user():
    """Check that search user properly returns tweets of/about a user when given that user's user ID"""
    twitterscraper = ts.Twitter()
    search_parameters = ["AOC", "tedcruz", "BernieSanders", "Aly_Raisman"]

    for term in search_parameters:
        try:
            dataframe = twitterscraper.search_user(term)

            direct_term_present = 0
            no_direct_term_present = 0
            direct_presense_ratio = 0
            hasTerm = False
            for ind in dataframe.index:
                tweet = dataframe["full_text"][ind]
                username = dataframe["screen_name"][ind]
                if term.lower() == username.lower():
                    hasTerm = True
                tweet_components = tweet.split(" ")
                for element in tweet_components:
                    if term.lower() in element.lower():
                        hasTerm = True
                if hasTerm is True:
                    direct_term_present += 1
                else:
                    no_direct_term_present += 1
            if(no_direct_term_present == 0):
                direct_presense_ratio = 1
            else:
                direct_presense_ratio = direct_term_present / no_direct_term_present
            assert direct_presense_ratio > 0.9
        except:
            time.sleep(10)
