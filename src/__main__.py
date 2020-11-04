
from data import accessingTwitterData

def classify():
    
    tweet_data = accessingTwitterData
    #Saving the return value from accessingtwitterdata
    
    #Print Tweets in list form.
    [tweet.text for tweet in tweet_data]
    user_data = [[tweet.user.screen_name] for tweet in tweet_data]
    #Saving the user's screen name seperately in order to search to see if it is verified
    #This will add another layer to test a Tweet's level of fake news
    


