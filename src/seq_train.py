from operator import mod
import os
import re
import time
import progressbar

import nltk
import numpy as np  
import pandas as pd  
import tensorflow as tf
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import LSTM, Dense, Dropout, Embedding
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.models import load_model
class MachineBuilder(object):

    def __init__(self):

        #api = TwitterClient()
        #trained_model = TrainingML()
        #sentiment = PoliticalClassification()
        self.df = pd.read_csv('./data/train.csv')
        self.test_df = pd.read_csv('./data/test.csv')
        self.voc_size = 5000

        self.sent_length = 20
        self.model_file = './models/finalized_model.sav'
        self.y = self.df['label']
        nltk.download('stopwords', quiet=True)

    def predict_truth(self, results_df):
        for dirname, _, filenames in os.walk('./data/'):
            for filename in filenames:
                print(os.path.join(dirname, filename))
        x = 0
        temp_results_df = results_df
        while x <= 2078:
            results_df = pd.concat([results_df, temp_results_df], ignore_index=True)
            x += 1
        X_final = np.array(self.prepare_tweets(results_df))
        X_train_final = X_final[:20800]

        X_test_final = X_final[20800:]
        y_final = np.array(self.y)
        X_test_final.shape
        X_train, X_test, y_train, y_test = train_test_split(
            X_train_final, y_final, test_size=0.33, random_state=42)
        print("Initiating")
        if os.path.exists(self.model_file):
            print("Trying to Find Saved Model Pt.1")
            model = load_model(self.model_file)
            print("Found!")
        else:
            print("Not Found")
            print("Training New Model Pt.1")
            
            model_build = self.build_model(self.prepare_tweets(self.build_dataframe()))
            model = self.train_model(
                X_train, X_test, y_train, y_test, model_build)
        print("Predicting")

        y_pred = (model.predict(X_test_final) > 0.5).astype("int32")
        print(y_pred.shape)
        
        print(y_pred.shape, self.test_df.id.shape)
        y_pred.shape, self.test_df.id.shape
        y_pred = y_pred.reshape(-1)
        print(type(y_pred))
        submission = pd.DataFrame(
            {'user': results_df.author, 'text': results_df.text, 'label': y_pred})
        print(submission.head())
        print(submission.shape)
        submission.to_csv('LSMT_model_work.csv', index=True)
        return submission

    def build_dataframe(self):
        print("Building Dataframe Pt.2")
        main_df = pd.concat(
            [self.df.drop(['label'], axis=1), self.test_df], axis=0)
        main_df.shape
        main_df.title.head(5)
        main_df.text.head(5)
        main_df.title = main_df.title.fillna(main_df['text'])
        main_df.isnull().sum()
        main_df.text = main_df.text.fillna(main_df.title)
        main_df.isnull().sum()
        main_df[main_df.author.isnull()]
        main_df.author = main_df.author.fillna('unknown')
        main_df.isnull().sum()
        main_df['total'] = main_df['title'] + \
            ' '+main_df['author']
        print("Dataframe Built")
        return main_df

    def prepare_tweets(self, main_df):
        X = main_df
        print("Preparing Tweets Pt.3")
        print("Messages Doing")
        messages = X.copy()
        messages.reset_index(inplace=True)
        print("Messages Done")

        print("Normalizing and Vectorizing Tweets")
        ps = PorterStemmer()
        corpus = []

        for i in progressbar.progressbar(range(0, len(messages))):
            review = re.sub('[^a-zA-Z]', ' ', messages['total'][i])
            review = review.lower()
            review = review.split()
            review = [ps.stem(
                word)for word in review if not word in stopwords.words('english')]
            review = ' '.join(review)
            corpus.append(review)
        corpus[0]
        one_represent = [one_hot(words, self.voc_size) for words in corpus]
        embedded_docs = pad_sequences(
            one_represent, padding='pre', maxlen=self.sent_length)
        print(embedded_docs[0])

        print("Tweets Prepared")
        return embedded_docs

    def build_model(self, embedded_docs):
        print("Building Model Pt.4")
        model = Sequential()
        y = self.df['label']

        model.add(Embedding(self.voc_size, 40, input_length=25))
        model.add(Dropout(0.3))
        model.add(LSTM(100))
        model.add(Dropout(0.3))
        model.add(Dense(64, activation='relu'))
        model.add(Dropout(0.3))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(loss='binary_crossentropy',
                           optimizer='adam', metrics=['accuracy'])
        print(model.summary())
        print(model.summary())
        len(embedded_docs), y.shape
        print("Model Built")
        return model

    def train_model(self, X_train, X_test, y_train, y_test, model):

        print("Training Model Pt.5")
        model.fit(X_train, y_train, validation_data=(
            X_test, y_test), epochs=20, batch_size=64)
        print("Saving Model")
        model.save(self.model_file)
        print("Model Trained and Saved")
        return model
