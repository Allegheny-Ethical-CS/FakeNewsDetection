import pytest

import src.preparedata as pd

def test_remove_URL():
    msg = "I can't believe what I saw on https://github.com/Allegheny-Ethical-CS/FakeNewsDetection the other day!"
    msg_url_removed = "I can't believe what I saw on  the other day!"
    preparedata = pd.PrepareData()
    new_msg = preparedata.remove_URL(msg)
    print(new_msg)
    assert new_msg == msg_url_removed

def test_remove_html():
    msg = "<strong> This bill will have an important effect on immigration reform </strong>"
    msg_html_removed = " This bill will have an important effect on immigration reform "
    preparedata = pd.PrepareData()
    new_msg = preparedata.remove_html(msg)
    print(new_msg)
    assert new_msg == msg_html_removed

def test_remove_emojis():
    msg = "Ask my cats what they think of this bill😻"
    msg_emoji_removed = "Ask my cats what they think of this bill"
    preparedata = pd.PrepareData()
    new_msg = preparedata.remove_emoji(msg)
    print(new_msg)
    assert new_msg == msg_emoji_removed

# hypothesis testing for what's not there?
def test_ntlk_process():
    original_msg = "<strong> This bill will have an important effect on \
     immigration reform </strong>.. Ask my cats what they think of this \
     bill😻,, I can't believe what I saw on https://github.com/Allegheny-Ethical-CS/FakeNewsDetection the other day!!!"
    preparedata = pd.PrepareData()
    new_msg = preparedata.ntlk_process(original_msg)
    assert len(new_msg) > 0

    double_punc_list = ["  ", "!!", "??", ".."]
    for element in double_punc_list:
        in_new_msg = element in new_msg
        assert in_new_msg == False

def test_prepare_data():
    
