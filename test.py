import json

data = '{"key":"M!n3"}'
data["key"] = 'value1'
json_data = json.dumps(data)
print(data, json_data)