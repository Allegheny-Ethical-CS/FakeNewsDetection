import os
import re
import time
from operator import mod

import nltk
from nltk.corpus.reader.chasen import test
import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport
import tensorflow as tf
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import LSTM, Dense, Dropout, Embedding
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.python.keras import callbacks
from tensorflow.python.keras.backend import print_tensor
import progressbar
import streamlit as st

class MachineBuilder(object):

    def __init__(self):
        self.trainfile = './data/train.csv'
        self.testfile = './data/test.csv'
        self.checkpoint_path = "./models/training_1/cp.ckpt"
        self.progress_bar = st.progress(0)
        self.voc_size = 5000

        self.sent_length = 25
        self.model_file = './models/finalized_model.sav'

    def preprocess_data(self):
        df = pd.read_csv(self.trainfile)
        test_df = pd.read_csv(self.testfile)
        df = df.sample(frac=1)
        test_df = test_df.sample(frac=1)
        df.title = df.title.fillna(df['text'])
        df.text = df.text.fillna(df.title)
        df.author = df.author.fillna('unknown')
        test_df.title = test_df.title.fillna(test_df['text'])
        test_df.text = test_df.text.fillna(test_df.title)
        test_df.author = test_df.author.fillna('unknown')
        df = df.fillna('')
        test_df = test_df.fillna('')
        df['total'] = df['title'] + ' ' + df['author']
        test_df['total'] = test_df['title'] + ' ' + test_df['author']
        X = df.drop('label', axis=1)
        y = df['label']
        print(X.shape)
        print(y.shape)
        msg = X.copy()
        msg_test = test_df.copy()
        return msg, msg_test, y

    def clean_data(self, msg, msg_test):
        ps = PorterStemmer()
        corpus = []
        corpus_test = []
        print("Downloading Stopwords")
        nltk.download('stopwords', quiet=True)
        print("Downloaded")
        for i in progressbar.progressbar(range(0, len(msg))):
            review = re.sub('[^a-zA-Z]', ' ', msg['total'][i])
            review = review.lower()
            review = review.split()
            review = [ps.stem(
                word)for word in review if word not in stopwords.words('english')]
            review = ' '.join(review)
            corpus.append(review)
            self.progress_bar.progress(i/len(msg))
        for i in progressbar.progressbar(range(0, len(msg_test))):
            review = re.sub('[^a-zA-Z]', ' ', msg_test['total'][i])
            review = review.lower()
            review = review.split()
            review = [ps.stem(
                word)for word in review if word not in stopwords.words('english')]
            review = ' '.join(review)
            corpus_test.append(review)
            self.progress_bar.progress(i/len(msg_test))
        one_rep = [one_hot(words, self.voc_size) for words in corpus]
        one_rep_test = [one_hot(words, self.voc_size) for words in corpus_test]
        embedded_docs = pad_sequences(
            one_rep, padding='pre', maxlen=self.sent_length)
        return embedded_docs

    def build_model(self):
        print("Building Model Pt.4")
        model = Sequential()
        model.add(Embedding(self.voc_size, 40, input_length=self.sent_length))
        model.add(Dropout(0.3))
        model.add(LSTM(1))
        model.add(Dropout(0.3))
        model.add(Dense(64, activation='relu'))
        model.add(Dropout(0.3))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(loss='binary_crossentropy',
                           optimizer='adam', metrics=['accuracy'])
        print(model.summary())
        print("Model Built")
        return model

    def train_model(self, model, embedded_docs, y):
        X_final = np.array(embedded_docs)
        y_final = np.array(y)
        X_final.shape, y_final.shape
        # Create a callback that saves the model's weights
        early_callback = tf.keras.callbacks.EarlyStopping(monitor='val_accuracy',
                                                        mode='auto',
                                                        patience=2,
                                                        baseline=None,
                                                        restore_best_weights=True
                                                        )
        cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=self.checkpoint_path,
                                                         save_weights_only=True,
                                                         verbose=1,)
        model.fit(X_final, y_final, epochs=30, batch_size=128,
                  validation_data=(X_final, y_final), callbacks=[early_callback])
        loss, acc = model.evaluate(X_final, y_final, verbose=2)
        print("Trained model, accuracy: {:5.2f}%".format(100 * acc))
        st.success("Trained model, accuracy: {:5.2f}%".format(100 * acc))
        return model

    def load_model(self):
        print("Initiating")
        with st.spinner("Searching for Model"):
            print("Trying to Find Saved Model Pt.1")
            model = self.build_model()
            if os.path.exists(self.checkpoint_path+".index"):
                print("Found!\nLoading Model")
                model.load_weights(self.checkpoint_path)

                st.success("Found Model\nLoading Model")
                return True, model
            else:
                print("Not Found\nTraining New Model")
                st.warning("Model Not Found\nBuilding a New One")
                return False, model

    def preprocess_tweets(self, results_df):
        tweets_df = results_df
        tweets_df.title = tweets_df.title.fillna(tweets_df['text'])
        tweets_df.text = tweets_df.text.fillna(tweets_df.title)
        tweets_df.author = tweets_df.author.fillna('unknown')
        tweets_df = tweets_df.fillna('')
        tweets_df['total'] = tweets_df['title'] + ' ' + tweets_df['author']
        tweets_test = tweets_df.copy()
        return tweets_test

    def clean_tweets(self, tweets_test):
        ps = PorterStemmer()
        corpus_test = []
        print("Downloading Stopwords")
        nltk.download('stopwords', quiet=True)
        print("Downloaded")
        for i in progressbar.progressbar(range(0, len(tweets_test))):
            review = re.sub('[^a-zA-Z]', ' ', tweets_test['total'][i])
            review = review.lower()
            review = review.split()
            review = [ps.stem(
                word)for word in review if word not in stopwords.words('english')]
            review = ' '.join(review)
            corpus_test.append(review)
            self.progress_bar.progress(i/len(tweets_test))
        one_rep_test = [one_hot(words, self.voc_size) for words in corpus_test]
        embedded_docs_tweets_test = pad_sequences(
            one_rep_test, padding='pre', maxlen=self.sent_length)
        return embedded_docs_tweets_test

    def predict_results(self, model, tweets_test, embedded_docs_tweets_test):
        test_final = embedded_docs_tweets_test
        y_pred = model.predict_classes(test_final)
        predictions = pd.DataFrame()
        predictions['author'] = tweets_test['author']
        predictions['text'] = tweets_test['text']
        predictions['label'] = y_pred
        predictions['label'] = predictions['label'].astype(int)
        predictions["label"] = ['Unreliable' if x==1 else 'Reliable' if x==0 else 'broken' for x in predictions['label']]
        return predictions

    def display_valid(self, results_df):
        model_exists, model = self.load_model()
        if model_exists:
            with st.spinner("Predicting Fake News"):
                tweets_test = self.preprocess_tweets(results_df)
                embedded_docs_tweets_test = self.clean_tweets(tweets_test)
                predictions = self.predict_results(
                    model, tweets_test, embedded_docs_tweets_test)
            st.success("Predictions Made")
            return predictions
        else:
            with st.spinner('Processing Data'):
                msg, msg_test, y = self.preprocess_data()
            st.success("Data Processed")
            with st.spinner('Cleaning Data'):
                embedded_docs = self.clean_data(msg, msg_test)
            st.success("Data Cleaned")
            with st.spinner('Training Model'):
                model = self.train_model(model, embedded_docs, y)
            st.success("Model Trained")
            with st.spinner("Predicting Fake News"):
                tweets_test = self.preprocess_tweets(results_df)
                embedded_docs_tweets_test = self.clean_tweets(tweets_test)
                predictions = self.predict_results(
                    model, tweets_test, embedded_docs_tweets_test)
            st.success("Predictions Made")
            return predictions
