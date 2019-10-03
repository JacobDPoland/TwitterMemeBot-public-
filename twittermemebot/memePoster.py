# This file follows along with the following video by freeCodeCamp
# https://www.youtube.com/watch?v=8u-zJVVVhT4

# This is the scipt that posts the images

import tweepy as tp  # used to access twitter through the api
import time
import os

# credentials to login to twitter api
# (generate your own lol)
consumer_key = ""  # API key
consumer_secret = ""  # API secret key
access_token = ""
access_secret = ""

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret) # next two preps for login
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)  # this logins to api

# iterate over pictures in memes folder
os.chdir('memes')  # change directory to memes folder
x = 0
for meme in os.listdir('.'):  # for every meme in the directory list
    api.update_with_media(meme)  # post meme
    time.sleep(5)  # wait 5 sec
    x += 1
    if x > 5:
        exit()
