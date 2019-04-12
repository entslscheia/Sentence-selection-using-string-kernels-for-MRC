import json

# for visualization
with open('data/SQuAD/splited/toy.json', 'r') as file:
    data = file.read()
obj = json.loads(data)
json.dump(obj, open('data/SQuAD/splited/toy.json', 'w'), indent=2)


# for generating toy example data
# with open('data/SQuAD1.1/train-v1.1.json') as f:
#     train = json.load(f)
#
# with open('data/SQuAD1.1/splited/toy.json', 'w') as outfile:
#     data = {}
#     data['data'] = []
#     data0 = {}
#     data0['title'] = train['data'][0]['title']
#     data0['paragraphs'] = []
#     data1 = {}
#     data1['context'] = train['data'][0]['paragraphs'][0]['context']
#     data1['qas'] = []
#     data1['qas'].extend(train['data'][0]['paragraphs'][0]['qas'][0:2])
#     data0['paragraphs'].append(data1)
#     data['data'].append(data0)
#     json.dump(data, outfile)