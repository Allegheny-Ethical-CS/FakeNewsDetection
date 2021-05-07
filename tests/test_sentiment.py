"""Test module for sentiment.py"""
import pytest
import src.sentiment as sn
from textblob import TextBlob

def test_get_nouns():
    text = """"I am planning to run for President in the 2024 election with Jill Biden as my vice president."""
    blob = TextBlob(text)
    assert (len(blob.noun_phases)) == 6
    
