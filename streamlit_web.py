import os
import pickle
from nltk.util import pr
from src.seq_train import MachineBuilder as ms
from numpy.lib.ufunclike import _fix_and_maybe_deprecate_out_named_y
import streamlit as st
import pandas as pd
import altair as alt
from src.twitterscraper import Twitter as ts
from src.preparedata import PrepareData as prep
import urllib
import pandas as pd
from pandas_profiling import ProfileReport

# @st.cache
def get_twitter_data():
    AWS_BUCKET_URL = "https://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
    return df.set_index("Region")


try:
    st.sidebar.title("Welcome to FakeNewsDetection!")
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
            with st.spinner("Collecting tweets"):
                results_df = ts().search_term(searching=text_input)
            st.success("Collected")
            with st.spinner("Formatting Tweets"):
                training_df = prep().build_Training_Results(results_df)
                results_df = prep().build_Results(results_df)
            st.success("Formatted")
        if data_retreive_method == 'Hashtag':
            with st.spinner("Collecting tweets"):
                results_df = ts().search_hashtag(searching=text_input)
            st.success("Collected")
            with st.spinner("Formatting Tweets"):
                training_df = prep().build_Training_Results(results_df)
                results_df = prep().build_Results(results_df)
            st.success("Formatted")
        if data_retreive_method == 'Username':
            with st.spinner("Collecting tweets"):
                results_df = ts().search_user(searching=text_input)
            st.success("Collected")
            with st.spinner("Formatting Tweets"):
                training_df = prep().build_Training_Results(results_df)
                results_df = prep().build_Results(results_df)
            st.success("Formatted")
            st.write(results_df)
        print("Entering Machine Learning")
        mach = ms()
        results = mach.display_valid(training_df)
        st.empty()
        st.write(results)
        design_report = ProfileReport(results)
        design_report.to_file(output_file='report.html')
    # df = get_twitter_data()
    # countries = st.multiselect(
    #     "Choose countries", list(df.index), ["China", "United States of America"]
    # )
    # if not countries:
    #     st.error("Please select at least one country.")
    # else:
    #     data = df.loc[countries]
    #     data /= 1000000.0
    #     st.write("### Gross Agricultural Production ($B)", data.sort_index())

    #     data = data.T.reset_index()
    #     data = pd.melt(data, id_vars=["index"]).rename(
    #         columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
    #     )
    #     chart = (
    #         alt.Chart(data)
    #         .mark_area(opacity=0.3)
    #         .encode(
    #             x="year:T",
    #             y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
    #             color="Region:N",
    #         )
    #     )
    #     st.altair_chart(chart, use_container_width=True)
except urllib.error.URLError as e:
    st.error(
        """
        **This demo requires internet access.**

        Connection error: %s
    """
        % e.reason
    )
