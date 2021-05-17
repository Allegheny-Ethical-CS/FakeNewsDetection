"""Check the correct preparation of twitter data for model consumption."""

import pytest
import string
import random
import pandas as pd
from datetime import datetime

import src.preparedata as prep
from src.twitterscraper import Twitter as ts

block_list = ["!!", " the ", "https://github.com/Allegheny-Ethical-CS", "github.com/Allegheny-Ethical-CS", "<bold>", "<italics>", " is ", ":", "{", "😻", "}", "  ", "!!", "??", ".."]


def test_remove_URL():
    """Check that remove URL function finds and removes URL in string."""
    msg = "I can't believe what I saw on https://github.com/Allegheny-Ethical-CS/FakeNewsDetection the other day!"
    msg_url_removed = "I can't believe what I saw on  the other day!"
    preparedata = prep.PrepareData()
    new_msg = preparedata.remove_URL(msg)
    assert new_msg == msg_url_removed

def test_remove_html():
    """Check that remove HTML function finds and removes HTML tags in string."""
    msg = "<strong> This bill will have an important effect on immigration reform </strong>"
    msg_html_removed = " This bill will have an important effect on immigration reform "
    preparedata = prep.PrepareData()
    new_msg = preparedata.remove_html(msg)
    assert new_msg == msg_html_removed

def test_remove_emojis():
    """Check that remove emoji function finds and removes emojis in a string."""
    msg = "Ask my cats what they think of this bill😻"
    msg_emoji_removed = "Ask my cats what they think of this bill"
    preparedata = prep.PrepareData()
    new_msg = preparedata.remove_emoji(msg)
    assert new_msg == msg_emoji_removed

def test_ntlk_process():
    """Check that ntlk process function finds and removes extraneous information such as html tags, urls, double punctuation, and stop words."""
    original_msg = "<strong> This bill will have an important effect on \
     immigration reform </strong>.. Ask my cats what they think of this \
     bill😻,, I can't believe what I saw on https://github.com/Allegheny-Ethical-CS/FakeNewsDetection the other day!!!"
    preparedata = prep.PrepareData()
    new_msg = preparedata.ntlk_process(original_msg)
    assert len(new_msg) > 0

    double_punc_list = ["  ", "!!", "??", ".."]
    for element in double_punc_list:
        assert not(element in new_msg)

    remove_function_list = ["<strong>", "</strong>", "😻", "https://github.com/Allegheny-Ethical-CS/FakeNewsDetection"]
    for element in remove_function_list:
        assert not(element in new_msg)


def test_ntlk_process_randomized():
    """Check that ntlk process function finds and removes extraneous information using random string generation."""
    for i in range(10):
        test_str = random_str(number_components = 15)
        assert len(test_str) > 0
        preparedata = prep.PrepareData()
        processed_str = preparedata.ntlk_process(test_str)
        for element in block_list:
            assert not(element in processed_str)


def test_prepare_data():
    """Check that prepare data properly processes each string in dataframe."""
    test_str = ""
    col_1_rows = []
    col_2_rows = []
    col_3_rows = []
    for i in range(10):
        col_1_rows.append(random_str())
        col_2_rows.append(random_str())
        col_3_rows.append(random_str())

    random_data = {'Column 1':col_1_rows, 'Column 2':col_2_rows, 'Column 3':col_3_rows}
    dataframe = pd.DataFrame(random_data)

    preparedata = prep.PrepareData()
    dataframe["Column 1"] = preparedata.prepare_data(dataframe, "Column 1")
    dataframe["Column 2"] = preparedata.prepare_data(dataframe, "Column 2")
    dataframe["Column 3"] = preparedata.prepare_data(dataframe, "Column 3")
    assert not(dataframe.empty)

    for ind in dataframe.index:
        for element in block_list:
            assert not(element in dataframe['Column 1'][ind])
            assert not(element in dataframe['Column 2'][ind])
            assert not(element in dataframe['Column 3'][ind])


def test_build_Results():
    """Check that build results function returns properly labelled and processed dataframe."""
    search_term_df = ts().search_term("court")
    assert not(search_term_df.empty)
    preparedata = prep.PrepareData()
    built_df = preparedata.build_Results(search_term_df)
    col_names = built_df.columns.values.tolist()
    assert "date" in col_names
    assert "text" in col_names
    assert "author" in col_names

    for ind in built_df.index:
        for element in block_list:
            assert not(element in built_df["author"][ind])
            assert not(element in built_df["text"][ind])


def random_str(number_components = 12):
    """Generate random string with some components that will need to be removed by ntlk process."""
    test_str = ""
    addition = ""
    component_id = 0
    component_len = 0
    for i in range(number_components):
        component_id = random.randint(0,14)
        component_len = random.randint(0,12)
        # random string generation credit to https://www.educative.io/edpresso/how-to-generate-a-random-string-in-python
        if(component_id == 0):
            addition = "  "
        if(component_id == 1):
            letters = string.ascii_lowercase
            addition = ''.join(random.choice(letters) for i in range(component_len))
        if(component_id == 2):
            letters = string.ascii_uppercase
            addition = ( ''.join(random.choice(letters) for i in range(component_len)) )
        if(component_id == 3):
            letters = string.ascii_letters
            addition = ( ''.join(random.choice(letters) for i in range(component_len)) )
        if(component_id == 4):
            letters = string.digits
            addition = ( ''.join(random.choice(letters) for i in range(component_len)) )
        if(component_id == 5):
            letters = string.punctuation
            addition = ( ''.join(random.choice(letters) for i in range(component_len)) )
        if(component_id == 6):
            addition = " https://github.com/Allegheny-Ethical-CS "
        if(component_id == 7):
            addition = "<bold>"
        if(component_id == 8):
            addition = "</italics>"
        if(component_id == 9):
            addition = "😻"
        if(component_id == 10):
            addition = " the "
        test_str += addition
        if(component_id == 11):
            addition = " is "
        if(component_id == 12):
            addition = "!!"
        if(component_id == 13):
            addition = " github.com/Allegheny-Ethical-CS "

    return test_str
