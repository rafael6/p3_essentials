__author__ = 'rafael'

import requests

r = requests.get('http://httpbin.org/get')
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.json())
