__author__ = 'rafael'

import requests
import json

r = requests.get('http://httpbin.org/get')
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.json())

# This will return a str
response = requests.get(uri)
print(response.text)

# This will retrun a Python collection dict in this example
# Method load decodes json to Python
# See json file for details
response = requests.get(uri)
response_json = json.loads(response.text)
print(response_json)
