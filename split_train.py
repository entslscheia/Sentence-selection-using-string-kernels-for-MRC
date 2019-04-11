# This file aims at split train-v1.1.json into multiple smaller files
import json

with open('data/SQuAD1.1/train-v1.1.json') as f:
    train = json.load(f)

num = len(train['data'])
num_i = int(num / 10)

for i in range(10):
    with open('data/SQuAD1.1/splited/' + str(i) + '.json', 'w') as outfile:
        data = {}
        data['data'] = []
        if i != 9:
            data['data'].extend(train['data'][i * num_i : (i + 1) * num_i])
        else:
            data['data'].extend(train['data'][i * num_i : num])

        json.dump(data, outfile)