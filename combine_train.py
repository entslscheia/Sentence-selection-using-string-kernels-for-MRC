# This file aims to combine several small files into an integral train file
import json

data = {'version': '2.0', 'data': []}
for i in range(10):
    with open('data/SQuAD/splited/' + str(i) + '.json') as f:
        data_i = json.load(f)
        data['data'].extend(data_i['data'])
with open('data/SQuAD/train-v2.0_augmented.json', 'w') as f:
    json.dump(data, f, indent=2)