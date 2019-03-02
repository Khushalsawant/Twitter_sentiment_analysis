
import tweepy
import datetime
from textblob import TextBlob

# keys and tokens from the Twitter Dev Console
consumer_key = 'CXwW3eLfEgcEUEbi7SK18Amyh'
consumer_secret = 'sKQpr6GZJed3hR40pzWNCQav08yUCMTqLwYMphbG2S3yuEgVvn'
access_token = '964883563131715585-XrManQyWNVoqZLBfnbhNIaOSyfDxMZx'
access_token_secret = 'LumTF49t4z3G5kW52uZXBIlCUlXNCwVbNniTcNqXkkeNw'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
[pos, neg] = [0,0]
sent = ''
result = 0
def query_twitter(q, max_tweets=50):
    for tweet in tweepy.Cursor(api.search, q=q).items(max_tweets):
        if (datetime.datetime.now() - tweet.created_at).days < 1:
            sentiment(tweet.text)
    print([pos, neg])
    print("Subject: "+ "'" + q + "'" + " is " + str("{0:.2f}".format(result)) + "% " + sent)
def sentiment(tweet):
    global pos
    global neg
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity >0:
        print('Positive: ' + tweet + '\n')
        pos = pos + 1
    elif analysis.sentiment.polarity < 0:
        print('Negative: ' + tweet + '\n')
        neg = neg + 1
    return sentiment_percent(pos, neg)
def sentiment_percent(pos, neg):
    global sent
    global result
    total = pos + neg
    if pos > neg:
        sent = "Positive"
        try:
            result = pos / total * 100
        except:
            print("An error occurred")
    else:
        sent = "Negative"
        try:
            result = neg / total * 100
        except:
            print("An error occurred")
    return {sent:result}
query_twitter('NOCIL', 500)
query_twitter('APAR', 500)