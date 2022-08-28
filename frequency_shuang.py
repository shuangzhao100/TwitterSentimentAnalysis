# this file takes 1 argument, the output.json
# python3 frequency_v2.py output.json

import json
import re
import sys

def clean_tweet(tweet):
    pattern_http = "\S*https:?\S*"
    pattern_email = "\S*@\S*\s?"
    pattern_punc = "[^\w\s]"
    pattern_num = "[0-9]"
    pattern_mulspace = "\s+"
    t1 = re.sub(pattern_http, '', tweet)
    t2 = re.sub(pattern_punc, '', t1)
    t3 = re.sub(pattern_num, '', t2)
    t4 = re.sub(pattern_mulspace, ' ', t3)
    t5 = t4[:-1]
    t6 = t5.rstrip()
    t7 = t6.lower()
    tweet = t7
    return tweet

def all_counts(tweets):
    tweets_clean = []
    pattern_http = "\S*https:?\S*"
    for tweet in tweets:
        t1 = re.sub(pattern_http, '', tweet)
        t2 = t1[:-1]
        t3 = t2.rstrip()
        t4 = t3.lower()
        tweets_clean.append(t4)
    # replace
    tweets = tweets_clean

    word_count = {}
    all_counts = 0
    for tweet in tweets:
        tokens = tweet.split()
        # print(tokens)
        for i in tokens:
            all_counts = 1 + all_counts
    return all_counts

def tweet_word_count(tweets):
    tweets_clean = []
    pattern_http = "\S*https:?\S*"
    for tweet in tweets:
        t1 = re.sub(pattern_http, '', tweet)
        t2 = t1[:-1]
        t3 = t2.rstrip()
        t4 = t3.lower()
        tweets_clean.append(t4)
    # replace
    tweets = tweets_clean
    word_count = {}
    for tweet in tweets:
        tokens = tweet.split()
        # print(tokens)
        for i in tokens:
            if i not in word_count.keys():
                # print('no')
                word_count[i] = 1
            else:
                word_count[i] = word_count[i] +1
    return word_count

# open the json file
file = open(sys.argv[1])
json_data = []
with file as f:
    for line in f:
        json_data.append(json.loads(line))

# clean the tweets
clean_tweets = []
for i in range(len(json_data)):
    text = clean_tweet(json_data[i]['data']['text'])
    clean_tweets.append(text)

tweets = clean_tweets

all_counts = all_counts(tweets)
term_count = tweet_word_count(tweets)

for i in term_count.keys():
    count = term_count[i]
    per = count/all_counts
    print(i, per)
