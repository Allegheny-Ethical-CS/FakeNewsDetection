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
