"""Test module for sentiment.py"""
import pytest
from textblob import TextBlob
import src.sentiment as sn

def test_get_nouns():
    text = """"I am planning to run for President in the 2024 election with Jill Biden as my vice president."""
    blob = TextBlob(text)
    assert (len(blob.noun_phases)) == 6
