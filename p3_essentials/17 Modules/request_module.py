__author__ = 'rafael'

import json
import requests

uri = 'https://jsonplaceholder.typicode.com/posts/1/'

# Some methods
response = requests.get(uri)
print(response.text) # returns the json as a str
print(response.status_code) # returns http status code an int
print(response.headers['content-type']) # returns header info as str
print(response.encoding) # returns encoding info as str
print(response.json()) # returns the json as a dict

# Desirializing/decoding json
response = requests.get(uri)
response_json = json.loads(response.text)
print(response_json) # returnsthe json as a dict

'''
json() vs loads()
They both deserialize/decode from json to Python object
json() is a requests thing where loads() is a JSON thing
loads works with utf-8 only, json() is more general 
some people prefer json() over loads() since it's more flexible
'''

