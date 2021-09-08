
import streamlit as st
import pandas as pd
import src.installation
from src.installation import installationPage
import src.home
from src.home import get_twitter_data


st.sidebar.title('Navigation')
pages = {'Installation':installationPage, 'Home': get_twitter_data}
choice = st.sidebar.selectbox("Choose your page: ",tuple(pages.keys()))
pages[choice]()
