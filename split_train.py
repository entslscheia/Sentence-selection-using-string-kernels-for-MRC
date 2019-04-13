# This file aims to split train.json into multiple smaller files
import json

with open('data/SQuAD/train-v2.0.json') as f:
    train = json.load(f)

num = len(train['data'])
print(num)
num_i = int(num / 10)

for i in range(10):
    with open('data/SQuAD/splited/' + str(i) + '.json', 'w') as outfile:
        data = {}
        data['version'] = '2.0'
        data['data'] = []
        if i != 9:
            data['data'].extend(train['data'][i * num_i : (i + 1) * num_i])
        else:
            data['data'].extend(train['data'][i * num_i : num])

        json.dump(data, outfile)