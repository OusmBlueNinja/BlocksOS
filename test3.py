import json


with open("data.json", "r") as x:
    data = json.load(x)

print(json.dumps(data, indent=2, sort_keys=True))

#print(data['data']['loggins'])
