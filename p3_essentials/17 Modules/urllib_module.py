__author__ = 'rafael'

import urllib.request
import urllib.parse  # To handle http encoding

# Example of raw read
'''
req = urllib.request.urlopen('https://www.google.com')
print(req.read())
'''

values = {'q': 'python programing tutorial'}  # Query values definition

data = urllib.parse.urlencode(values)  # Query construct

url = 'https://www.google.com/search?'+data  # URL

# data = data.encode('utf-8')  # Convert query construct to utf-8

headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (x11; Linux i686)'

req = urllib.request.Request(url, headers=headers)  # Complete query

resp = urllib.request.urlopen(req)  # Open the connection

resp_data = resp.read()  # Read the content from connection

print(resp_data)