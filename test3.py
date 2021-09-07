import json


data = json.load(open("data.json"))

print(json.dumps(data, indent=1, sort_keys=True))

print(data['data']['misc'])
