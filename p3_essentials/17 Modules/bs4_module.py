from bs4 import BeautifulSoup
import urllib.request
import time

req = urllib.request.urlopen('http://www.nationaljournal.com/politics?rss=1')

xml = BeautifulSoup(req, 'xml')  # use 'xml' since html is the default

for i in xml.findAll('link')[1:]:  # links is the xml tag; [1:] everything after the first one
    url = i.text  # Without .text tags are included in output
    news = urllib.request.urlopen(url)
    #print(news)
    #print('#' * 80)
    page = BeautifulSoup(news)
    for p in page.findAll('p'):
        print(p.text)
    time.sleep(10)



