import json
import requests

#json.loads()
#convert a json string in a dictinary object
#Your JSON is an array with a single object inside, so
#  when you read it in you get a list with a dictionary inside.
#  You can access your dictionary by accessing item 0 in the list, as shown below:
json1_data = json.loads(json1_str)[0]
#Now you can access the data stored in datapoints just as you were expecting:
datapoints = json1_data['datapoints']


#json.load()
#how to serilize a json object into a dict
import os
import json


def get_template(template_name):
    try:
        template_path = os.path.join(
            os.path.dirname(__file__),
            'templates',
            template_name
        )
        with open(template_path, 'r') as template_file_fd:
            template = json.load(template_file_fd)
        return template
    except IOError:
        print('An IOError has occurred! path: {} file: {}'.format(
            template_path, template_name))



print(get_template('my.json'))

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