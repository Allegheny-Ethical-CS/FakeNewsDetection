"""Test module for sentiment.py"""
import pytest
from textblob import TextBlob
import src.sentiment as sn

def test_get_nouns():
    PoliticalClassification = sn.PoliticalClassification()
    text = """"The North America relief grant will be passed next week by Joseph Lemmis."""
    blob = TextBlob(text)
    nouns = PoliticalClassification.get_nouns(blob)
    assert (len(nouns)) > 0
    assert "relief grant" in nouns
    assert "america" in nouns
    assert "joseph lemmis" in nouns
