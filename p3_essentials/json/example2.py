# How to process json streams

import json
import requests

request = requests.get('uri')
request_text = request.txt

data = json.loads(request_text)
print(data)