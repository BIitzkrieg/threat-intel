#!/bin/python
import tweepy
import iocextract
import re

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
tweet_mode = 'extended'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

id = "user_id_here"
user = api.user_timeline(id, count=100, tweet_mode='extended')
iocList = []
for tweet in user:
    #print(tweet.full_text)
    #adjust to "true" for "unsafe" ioc's
    for ioc in iocextract.extract_iocs(str(tweet.full_text), refang=False):
        if re.match(r"(?!https:\/\/t\.co|127\.0\.0\.1)", str(ioc)):
            #print(ioc)
            iocList.append(ioc)

stripSpace = [x.strip(' ') for x in iocList]
strippedIOC = list(set(stripSpace))
for ioc in strippedIOC:
     print(ioc)
