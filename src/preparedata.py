"""Class to return dataframe of tweets with unwanted words/characters removed
given dataframe of original tweets."""


import re
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer

# pylint: disable=R0201, C0103


class PrepareData():
    """Return dataframe of tweets with unwanted words/characters removed given
    dataframe of original tweets."""

    def __init__(self):
        """Class constructor, initializes normalization objects."""

        nltk.download('stopwords')
        self.stemmer = LancasterStemmer()
        self.stop_words = stopwords.words('english')
        self.lemmatizer = WordNetLemmatizer()

    def remove_URL(self, text):
        """Return given string with any URLs removed."""

        url = re.compile(r'https?://\S+|www\.\S+')
        return url.sub(r'', text)

    def remove_html(self, text):
        """Return given string with any html tags removed."""
        html = re.compile(r'<.*?>')
        return html.sub(r'', text)

    def remove_emoji(self, text):
        """Return given string with any unicode emojis removed."""

        emoji_pattern = re.compile("["u"\U0001F600-\U0001F64F"  # emoticons
                                   u"\U0001F300-\U0001F5FF"  # symbols
                                   u"\U0001F680-\U0001F6FF"  # map/transport
                                   u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                   u"\U00002702-\U000027B0"
                                   u"\U000024C2-\U0001F251"
                                   "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', text)

    def ntlk_process(self, text):
        """Normalize given string."""

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
        """Normalize each string in a given dataframe column."""

        print("Preparing Data")
        dataframe[column_name] = dataframe[column_name].apply(
            lambda x: self.ntlk_process(str(x)))
        print("\033[A")
        return dataframe[column_name]

    def build_Training_Results(self, dataframe):
        """Restructure dataframe for comprehension by classification model."""

        training_df = pd.DataFrame(columns=["id", "title", "author", "text"])
        training_df['id'] = dataframe['index']
        training_df['title'] = ''
        training_df['author'] = dataframe['user_id']
        training_df['text'] = dataframe['full_text']
        training_df.shape
        training_df.title.head(5)
        training_df.text.head(5)
        training_df.title = training_df.title.fillna(training_df['text'])
        training_df.isnull().sum()
        training_df.text = training_df.text.fillna(training_df.title)
        training_df.isnull().sum()
        training_df[training_df.author.isnull()]
        training_df.author = training_df.author.fillna('unknown')
        training_df.isnull().sum()
        training_df['total'] = training_df['title']
        return training_df

    def build_Results(self, dataframe):
        """Restructure returned dataframe to most user-friendly way."""

        results_df = dataframe
        results_df.set_index('index')
        results_df = results_df.drop('index', axis=1)
        results_df = results_df[['created_at', 'user_id', 'full_text']]
        results_df = results_df.rename(columns={
            'created_at': 'date',
            'user_id': 'author',
            'full_text': 'text'
        })
        results_df['date'] = pd.to_datetime(results_df['date']).dt.date
        results_df['text'] = self.prepare_data(results_df, 'text')
        results_df['author'] = self.prepare_data(results_df, 'author')

        print("Built Dataframe")
        return results_df
