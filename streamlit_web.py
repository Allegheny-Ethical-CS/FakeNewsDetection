
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
import src.installation
from src.installation import installationPage
import src.home
from src.home import get_twitter_data


st.sidebar.title('Navigation')
pages = {'Installation':installationPage, 'Home': get_twitter_data}
choice = st.sidebar.selectbox("Choose your page: ",tuple(pages.keys()))
pages[choice]()
