# this file takes 2 argument, the first is the AFINN-111.txt
# the second is the output.json
# python3 tweet_sentiment_shuang.py AFINN-111.txt output.json

import json
import re
import sys

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

def main():
    sent_file = open(sys.argv[1])
    #tweet_file = open(sys.argv[2])
    # hw()
    # lines(sent_file)
    # lines(tweet_file)

if __name__ == '__main__':
    main()

# generate a sentiment dictionary
sent_file = open(sys.argv[1])
sent_dict = generate_sent_dict(sent_file)
# print(sent_dict)

file = open(sys.argv[2])
json_data = []
with file as f:
    for line in f:
        json_data.append(json.loads(line))

clean_tweets = []
for i in range(len(json_data)):
    text = clean_tweet(json_data[i]['data']['text'])
    clean_tweets.append(text)

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

scores = cal_sent(clean_tweets)

for i in scores:
    print(i)
