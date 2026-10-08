#dumps() python -> json (str)
#loads() json -> python (str)
#dump() save python object as json to the file
#load() file.json -> python
import json

user = {"username": "admin", "age": "25", "is_admin": True }
json_str = json.dumps(user)
print(json_str)
print(type(json_str))

user = json.loads(json_str)
print(user)
print(type(user))

test_config = {
    "url": "http://127.0.0.1:5000/",
    "username": "newbie",
    "password": "Aa123!",
    "timeout": 20 }

with open("test_config.json", "w", encoding="utf-8") as file:
    json.dump(test_config, file, indent=4, ensure_ascii=False)

with open("test_config.json", "r", encoding="utf-8") as file:
    config = json.load(file)

print(config)
print(type(config))
print(config["url"])