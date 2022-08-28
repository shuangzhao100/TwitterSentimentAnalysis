# this file takes 2 argument, the first is the AFINN-111.txt
# the second is the output.json
# python3 term_v2.py AFINN-111.txt output.json

import sys
import re
import json


def generate_sent_dict(file):
    sent = file.readlines()
    sent_dict = {}
    for line in sent:
        if line[-1] == '\n':
            x = line.partition('\t')[2]
            length = len(line.partition('\t')[2])
            x = x[:length - 1]
            sent_dict[line[:-4]] = x
        else:
            sent_dict[line[:-2]] = line[-1]
    return sent_dict


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

def tweet_score(tweet):
    tokens = tweet.split()
    tweet_score = 0
    for i in tokens:
        if i in sent_dict.keys():
            tweet_score = tweet_score + int(sent_dict.get(i))
        else:
            tweet_score = tweet_score
    return tweet_score

def cal_total_score(new_term):
    total_score = 0
    for tweet in tweets:
        if new_term in tweet:
            total_score = total_score + tweet_score(tweet)
        else:
            total_score = total_score + 0
    return total_score

def count_existing(tweet):
    count = 0
    tokens = tweet.split()
    for i in tokens:
        if i in sent_dict.keys():
            count = count + 1
        else:
            count = count + 0
    return count

def cal_total_count(new_term):
    total_count = 0
    for tweet in tweets:
        if new_term in tweet:
            total_count = total_count + count_existing(tweet)
        else:
            total_count = total_count + 0
    return total_count

def cal_new_term(new_term):
    if new_term in sent_dict.keys():
        score_newterm = int(sent_dict.get(new_term))
        print('This term exists in the AFINN-111 file')
    else:
        score = cal_total_score(new_term)
        count = cal_total_count(new_term)
        if count == 0:
            score_newterm = 0.0
        else:
            score_newterm = score/count
        # print('This is a new term')
    return score_newterm

def cal_sent(tweets):
    score_list = []
    for tweet in tweets:
        tokens = tweet.split()
        tweet_score = 0
        for i in tokens:
            if i in sent_dict.keys():
                tweet_score = tweet_score + int(sent_dict.get(i))
            else:
                tweet_score = tweet_score
        # print(tweet_score)
        score_list.append(tweet_score)
    return score_list

def main():
    sent_file = open(sys.argv[1])


if __name__ == '__main__':
    main()

# generate a sentiment dictionary
sent_file = open(sys.argv[1])
sent_dict = generate_sent_dict(sent_file)

# open the json file
file = open(sys.argv[2])
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

# apply the function to all tokens in tweets
for tweet in tweets:
    tokens = tweet.split()
    for i in tokens:
        if i in sent_dict.keys():
            print(i,' This term exists in the AFINN-111 with a score of', int(sent_dict.get(i)))
        else:
            print(i, round(cal_new_term(i),4))