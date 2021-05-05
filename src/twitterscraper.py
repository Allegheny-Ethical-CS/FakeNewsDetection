
import os

import pandas as pd
from bluebird import BlueBird
from bluebird.scraper import BlueBird
from io import StringIO



class Twitter(object):

    def __init__(self):
        self.col_names32 = StringIO("""created_at,id,id_str,full_text,truncated,display_text_range,entities,source,in_reply_to_status_id,in_reply_to_status_id_str,in_reply_to_user_id,in_reply_to_user_id_str,in_reply_to_screen_name,user_id,user_id_str,geo,coordinates,place,contributors,is_quote_status,retweet_count,favorite_count,conversation_id,conversation_id_str,favorited,retweeted,possibly_sensitive,possibly_sensitive_editable,lang,supplemental_lang,,self_thread""")
    #api = TwitterClient()
    #trained_model = TrainingML()
    #sentiment = PoliticalClassification()

        self.user_results = "./data/results.csv"


    def search_term(self, searching):
        index = 0
        query = {
            'fields': [
                {'items': [searching]},
            ]
        }
        results_df = pd.DataFrame(columns=['index','created_at', 'full_text', 'user_id'])
        for tweet in BlueBird().search(query):
            index += 1
            res = {"created_at":tweet['created_at'],"full_text":tweet['full_text'],"user_id":tweet['user_id']}
            print(res)
            results_df = results_df.append(res, ignore_index=True)
            print(index)
            if index == 50:
                print("Tweets Found!!")
                results_df.set_index('index')
                results_df = results_df.drop('index', axis=1)
                print(results_df.head)
                
                return results_df
        


    def search_hashtag(self, searching):
        try:
            os.remove('./data/results.csv')
            os.remove('./data/temp.csv')
        except:
            print()
        index = 0

        query = {
            'fields': [
                {'items': [searching], 'target':'hashtag'},
            ]
        }
        results_df = pd.DataFrame()
        for tweet in BlueBird().search(query):
            index += 1
            res = {"created_at":tweet['created_at'],"full_text":tweet['full_text'],"user_id":tweet['user_id']}
            print(res)
            results_df.append(res,ignore_index=True)
            print(index)
            if index == 50:
                print("Tweets Found!!")
                print(results_df.head)
                return results_df
            # with open(self.user_results, 'a') as f:
            #     df.to_csv(f, header=None, index=False)
            # if index == 50:
            #     dummy_file = self.user_results + '.bak'
            #     with open(self.user_results, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
            #         write_obj.write(self.col_names32 + '\n')
            #         for line in read_obj:
            #             write_obj.write(line)
            #     os.remove(self.user_results)
            #     os.rename(dummy_file, self.user_results)
            os.remove("./data/temp.json")
            return results_df


    def search_user(self, searching):
        try:
            os.remove('./data/results.csv')
            os.remove('./data/temp.csv')
        except:
            print()
        index = 0

        query = {
            'fields': [
                {'items': [searching], 'target':'from'},
            ]
        }
        results_df = pd.DataFrame()
        for tweet in BlueBird().search(query):
            index += 1
            res = {"created_at":tweet['created_at'],"full_text":tweet['full_text'],"user_id":tweet['user_id']}
            print(res)
            results_df.append(res,ignore_index=True)
            print(index)
            if index == 50:
                print("Tweets Found!!")
                print(results_df.head)
                return results_df

# def main():
#     try:
#         os.remove('./data/results.csv')
#         os.remove('./data/temp.csv')
#     except:
#         print()
#     print("Welcome to the Fake News Dection Program! \n")
#     print("Would you like to search by:\nkeyword\nhashtag\nuser")
#     done = False
#     while done == False:
#         choice = input("keyword/hashtag/user: ")
#         if choice == "keyword":
#             search_term()
#             done = True
#         elif choice == "hashtag":
#             search_hashtag()
#             done = True
#         elif choice == "user":
#             search_user()
#             done = True
#         else:
#             print("Sorry, Bad Input. Please Enter One of the Options Below")
#             done = False
#     try:
#         os.remove('data/temp.json')
#     except:
#         print()


# if __name__ == '__main__':
#     # calls main function
#     main()
