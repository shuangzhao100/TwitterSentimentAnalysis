# python3 happy_v2.py AFINN-111.txt output.json
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


def cal_sent(tweet):
    tokens = tweet.split()
    tweet_score = 0
    for i in tokens:
        if i in sent_dict.keys():
            tweet_score = tweet_score + int(sent_dict.get(i))
        else:
            tweet_score = tweet_score
    # print(tweet_score)
    return tweet_score

def hasMatch(text):
    text_list = text.split(',')
    if len(text_list) >0:
        state = text_list[-1]
        return states.__contains__(state)
    return false

def main():
    sent_file = open(sys.argv[1])
    # tweet_file = open(sys.argv[2])
    # hw()
    # lines(sent_file)
    # lines(tweet_file)


if __name__ == '__main__':
    main()

# dictionary containing state information
states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

# generate a sentiment dictionary
sent_file = open(sys.argv[1])
sent_dict = generate_sent_dict(sent_file)

# open the json file and load json to a list of dictionary
file = open(sys.argv[2])
json_data = []
with file as f:
    for line in f:
        json_data.append(json.loads(line))

pair_list = []
for i in range(len(json_data)):
    if json_data[i]['data']['lang'] == 'en':
        text = clean_tweet(json_data[i]['data']['text'])
        score = cal_sent(text)
        try:
            location = json_data[i]['includes']['users'][0]['location']
            pair = (location,score) # pair is a tuple
            pair_list.append(pair)
        except:
            continue
    else:
        continue




# if the location contains abbreviations of states, for example, "WA"
# include it in the sent_state dictionary and accumulate the sentiment score of the tweet
sent_state = {}
for i in range(len(pair_list)):
    location_list = (pair_list[i][0].split())
    count = 0
    for x in location_list:
        if hasMatch(x):
            # print(x, pair_list[i][-1])
            count = count + 1
            if x not in sent_state.keys():
                sent_state[x] = pair_list[i][-1]
            else:
                sent_state[x] = sent_state.get(x) + pair_list[i][-1]


count_state = {}
for i in range(len(pair_list)):
    location_list = (pair_list[i][0].split())
    count = 0
    for x in location_list:
        if hasMatch(x):
            count_state[x] = count + 1

# calculate the average sentiment scores by state
avg_score = {}
for x in sent_state.keys():
    avg_score[x] = sent_state[x]/count_state[x]

# filter out the happiest state
sorted_dict = {}
sorted_keys = sorted(avg_score, key=avg_score.get,reverse=True)[:1]

for w in sorted_keys:
    sorted_dict[w] = avg_score[w]

for key, value in sorted_dict.items():
    print(key, ' ', value)