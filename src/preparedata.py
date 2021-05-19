import re
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer

# pylint: disable=R0201, C0103

class PrepareData():

    def __init__(self):
        nltk.download('stopwords')
        self.stemmer = LancasterStemmer()
        self.stop_words = stopwords.words('english')
        self.lemmatizer = WordNetLemmatizer()

    def remove_URL(self, text):
        url = re.compile(r'https?://\S+|www\.\S+')
        return url.sub(r'', text)

    def remove_html(self, text):
        html = re.compile(r'<.*?>')
        return html.sub(r'', text)

    def remove_emoji(self, text):
        emoji_pattern = re.compile("["u"\U0001F600-\U0001F64F"  # emoticons
                                   u"\U0001F300-\U0001F5FF"  # symbols
                                   u"\U0001F680-\U0001F6FF"  # map/transport
                                   u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                   u"\U00002702-\U000027B0"
                                   u"\U000024C2-\U0001F251"
                                   "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', text)

    def ntlk_process(self, text):

        text = self.remove_emoji(text)
        text = self.remove_html(text)
        text = self.remove_URL(text)
        text = text.lower()
        text = re.sub(r'[:"$%&\*+,-/:;<=>@\\^_`{|}~]+', '', text)
        text = re.sub(r'&amp;?', r'and', text)  # replace & -> and
        text = re.sub(r"'", "", text)
        text = re.sub(r"'s", "", text)
        text = re.sub(' +', ' ', text).strip()  # Remove and double spaces
        text = re.sub(r'[!]+', '!', text)
        text = re.sub(r'[?]+', '?', text)
        text = re.sub(r'[.]+', '.', text)
        tokens = []
        for token in text.split():
            if token not in self.stop_words:
                tokens.append(self.lemmatizer.lemmatize(token))
        return " ".join(tokens)

    def prepare_data(self, dataframe, column_name):
        print("Preparing Data")
        dataframe[column_name] = dataframe[column_name].apply(
            lambda x: self.ntlk_process(str(x)))
        print("\033[A")
        return dataframe[column_name]

    def build_Results(self, dataframe):
        results_df = dataframe
        results_df = results_df[['created_at', 'user_id', 'full_text']]
        results_df = results_df.rename(columns={
        'created_at': 'date',
        'user_id': 'author',
        'full_text': 'text'})
        results_df['date'] = pd.to_datetime(results_df['date']).dt.date
        results_df['text'] = self.prepare_data(results_df, 'text')
        results_df['author'] = self.prepare_data(results_df, 'author')
        print("Built Dataframe")
        return results_df
