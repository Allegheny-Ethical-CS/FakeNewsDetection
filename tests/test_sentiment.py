"""Test module for sentiment.py"""
import pytest
from textblob import TextBlob
import src.sentiment as sn

# issue: currently isn't working because of lack of file for preparadata to initialize from
def test_get_nouns():
    text = """"I am planning to run for President in the 2024 election with Jill Biden as my vice president."""
    # PoliticalClassification = sn.PoliticalClassification()
    blob = TextBlob(text)
    # nouns = PoliticalClassification.get_nouns(blob)
    # print(nouns)
    # assert (len(nouns)) == 6
