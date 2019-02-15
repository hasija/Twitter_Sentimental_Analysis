import tweepy
import numpy as np
import pandas as pd
import numpy as np
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
consumer_key = '***'
consumer_secret = '***'
access_token = '***'
access_token_secret = '***'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
tweets = api.search('ElClassico', count = 200)
data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
pd.options.display.max_colwidth = 10000
sid = SentimentIntensityAnalyzer()
listy = []
for index, row in data.iterrows():
	score = sid.polarity_scores(row.Tweets)
	listy.append(score)
data['polarity_scores'] = np.array(listy)[:]
print (data)
