"""Test module for sentiment.py"""
import time
from textblob import TextBlob
import src.sentiment as sn
from src.twitterscraper import Twitter as ts

# pylint: disable=W0702, C0103


def test_get_nouns():
    PoliticalClassification = sn.PoliticalClassification()
    text = """"The North America relief grant will be passed next week by Joseph Lemmis."""
    blob = TextBlob(text)
    nouns = PoliticalClassification.get_nouns(blob)
    assert (len(nouns)) > 0
    assert "relief grant" in nouns
    assert "america" in nouns
    assert "joseph lemmis" in nouns


# test driven development of get tweet sentiment
def test_get_tweet_sentiment():
    PoliticalClassification = sn.PoliticalClassification()

    tweet_count = 0
    left_leaning = 0
    right_leaning = 0
    try:
        search_term_df = ts().search_term("Facebook")
    except:
        time.sleep(10)
        search_term_df = ts().search_term("Facebook")
    for ind in search_term_df.index:
        tweet_count += 1
        ratio = PoliticalClassification.get_tweet_sentiment(search_term_df["full_text"][ind])
        if ratio == -1:
            left_leaning += 1
        if ratio == 1:
            right_leaning += 1
    # assert ((right_leaning+left_leaning)/tweet_count) >= 0.6
    # assert (right_leaning/tweet_count) >= 0.3
    # assert (left_leaning/tweet_count) >= 0.3
