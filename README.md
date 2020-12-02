# FakeNewsDetection
Identify and label Tweets as Fake News

# Installation:
In order to use this tool you must first the __tweepy__ and __textblob__ libraries.
```shell
pip install tweepy
```
and then,

```shell
pip install textblob
```

# About
This project was completed in conjunction with the Mozilla Foundation for the Mozilla Project, which is seeking to build ethical tools in the world of computer science. This ethical tool will search through Tweets and attempt to label them as "right", "left", "centrist" and also add a level of fake news detection to them. While Twitter is currently working on this feature, it is not completely employed at the moment. The goal of this feature is to minimize the amount of fake news that the public recieves from social media outlets.

This detection is done by searching the selected user's tweets for various words which indicate fake news, such as "most", "least", etc.
