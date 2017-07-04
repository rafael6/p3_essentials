import json
import requests

# Jason representation of an object
obj = {u"answer": [42.5], u"abs": 42}
print(json.dumps(obj))  # {"answer": [42.5], "abs": 42}

# Loading: loads to load from a string; load to load from a stream
obj_json = u'{"answer": [42.5], "abs": 42}'
obj = json.loads(obj_json)
print(repr(obj))  # {"answer": [42.5], "abs": 42}

#Indentation
obj = {u"answer": [42.5], u"abs": 42}
print(json.dumps(obj, indent=4))

# Json can only store the following objects: str, numbers, bools, None, list, dicts
# Objects of a custom class need to be converted


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

def jdefault(o):
    return o.__dict__

alice = User('Alice A. Adams', 'secret')
print(json.dumps(alice, default=jdefault))  # {"name": "Alice A. Adams", "password": "secret"}


# json as parameters

url = 'https://some.com/api'
params = {'element': 'google.com', 'kind': 'VIP'}
resp = requests.get(url=url, params=params)
data = json.loads(resp.txt)