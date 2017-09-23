# bs4_1.py

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page1.html")

# print(html.read())
# print(html.read().decode('utf-8'))

bsObj = BeautifulSoup(html.read(), 'lxml')
print(bsObj)
