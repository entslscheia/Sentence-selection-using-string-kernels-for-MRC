import json

with open('./data/SQuAD1.1/dev-v1.1.txt', 'r') as file:
    data = file.read()
obj = json.loads(data)
json.dump(obj, open('./data/SQuAD1.1/dev-v1.1.txt', 'w'), indent=2)