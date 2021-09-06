
import sys
import os
import pickle
from nltk.util import pr
from src.seq_train import MachineBuilder as ms
from numpy.lib.ufunclike import _fix_and_maybe_deprecate_out_named_y

import streamlit as st
import pandas as pd
from src.twitterscraper import Twitter as ts
from src.preparedata import PrepareData as prep
import urllib
import pandas as pd
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import webbrowser

# pylint: disable=R0201, C0103
# @st.cache
def get_twitter_data():
    AWS_BUCKET_URL = "https://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
    return df.set_index("Region")


try:
    st.sidebar.title("Welcome to FakeNewsDetection")
    st.sidebar.write("FakeNewsDetection will allow you to search through live Tweets from Twitter via keyword, username, or hashtag. The BOT will then perform sentiment, validity, and politial analysis on the Tweets!")
    data_retreive_method = st.sidebar.selectbox(
        "How would you like to search Twitter?",
        [
            "Keyword",
            "Hashtag",
            "Username",
        ],
    )
# Alternative syntax, declare a form and use the returned object
    form = st.form(key='user_search')
    text_input = form.text_input(label='What would you like to search')
    submit_button = form.form_submit_button(label='Submit')

# st.form_submit_button returns True upon form submit
    if submit_button:
        if data_retreive_method == 'Keyword':
            with st.empty():
                with st.spinner("Collecting tweets"):
                    results_df = ts().search_term(searching=text_input)
                st.success("Collected")
            with st.empty():
                with st.spinner("Formatting Tweets"):
                    training_df = prep().build_Training_Results(results_df)
                    results_df = prep().build_Results(results_df)
                st.success("Formatted")
                st.table(results_df)
        if data_retreive_method == 'Hashtag':
            with st.empty():
                with st.spinner("Collecting tweets"):
                    results_df = ts().search_hashtag(searching=text_input)
                st.success("Collected")
            with st.empty():
                with st.spinner("Formatting Tweets"):
                    training_df = prep().build_Training_Results(results_df)
                    results_df = prep().build_Results(results_df)
                st.success("Formatted")
                st.table(results_df)
        if data_retreive_method == 'Username':
            with st.empty():
                with st.spinner("Collecting tweets"):
                    results_df = ts().search_user(searching=text_input)
                st.success("Collected")
            with st.empty():
                with st.spinner("Formatting Tweets"):
                    training_df = prep().build_Training_Results(results_df)
                    results_df = prep().build_Results(results_df)
                st.success("Formatted")
                st.table(results_df)
        print("Entering Machine Learning")
        mach = ms()
        results = mach.display_valid(training_df)
        st.empty()
        st.table(results)
        design_report = ProfileReport(results)
        design_report.to_file(output_file='report.html')
        webbrowser.open_new_tab(url="report.html")

except urllib.error.URLError as e:
    st.error(
        """
        **This demo requires internet access.**

        Connection error: %s
    """
        % e.reason
    )
