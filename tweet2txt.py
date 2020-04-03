import twitter
import tweepy 
import re, itertools
import json
import nltk
from nltk.corpus import stopwords
import unicodedata


def analyze(handle):
    file1 = open("myfile.txt","w")
    consumer_key = ''
    consumer_secret = ''
    access_key = ''
    access_secret = ''

    
    # Authorization to consumer key and consumer secret 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    # Access to user's access key and access secret 
    auth.set_access_token(access_key, access_secret)
    # Calling api 
    api = tweepy.API(auth) 
    # 200 tweets to be extracted 
    number_of_tweets=200
    statuses = api.user_timeline(screen_name=handle,count=200,tweet_mode="extended")
    print(type(statuses))
    for st in statuses:
        jas=json.dumps(st._json)
    
    #print(jas)

    #statuses = twitter_api.GetUserTimeline(screen_name=handle, count=2000, include_rts=False)
    text=""
    for s in statuses:
        #print(type(s))
        if (s.lang=='en'):
            
            text += s.full_text
            
            print("\nRemove urls\n")
            text =  re.sub(r'https?:\/\/.*[\r\n]*', ' ', text, flags=re.MULTILINE)
            
            
            #print(text)
    text=str(text.encode("utf-8"))
    file1.writelines(text)
         
    

    #print(text)
    
    #Use normal file handeling codes to solve encoding problems
    
    file1.close()
analyze('@RobertDowneyJr')
