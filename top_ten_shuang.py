# python3 top10_v2.py output.json
import json
import sys
file = open(sys.argv[1])
json_data = []
with file as f:
    for line in f:
        json_data.append(json.loads(line))
tag_list = []
for i in range(len(json_data)):
    if json_data[i]['data']['lang'] == 'en':
        try:
            for x in range(len(json_data[i]['data']['entities']['hashtags'])):
                tag = json_data[i]['data']['entities']['hashtags'][x]['tag']
                tag_list.append(tag)
        except:
            pass
    else:
        continue
# clean the hashtags
tag_cleaned = []
for tag in tag_list:
    tag2 = tag.lower()
    tag_cleaned.append(tag2)
hashtag_dict = {}
for i in tag_cleaned:
    if i not in hashtag_dict:
        hashtag_dict[i] = 1
    else:
        hashtag_dict[i] = hashtag_dict[i]  + 1
# sort and print top 10 hashtags
sorted_dict = {}
sorted_keys = sorted(hashtag_dict, key=hashtag_dict.get,reverse=True)[:10]
for w in sorted_keys:
    sorted_dict[w] = hashtag_dict[w]

for key, value in sorted_dict.items():
    print(key, ' ', value)