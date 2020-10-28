
from data import accessingTwitterData

def classify():
    
    tweet_data = accessingTwitterData
    #
    
    #Print Tweets in list form.
    [tweet.text for tweet in tweet_data]
    user_data = [[tweet.user.screen_name] for tweet in tweet_data]

