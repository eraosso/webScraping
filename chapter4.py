
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

url = "http://www.pythonscraping.com/pages/page1.html"
html = urlopen("http://pythonscraping.com/pages/page1.html")
bs = BeautifulSoup(html.read(), "html.parser")
print(bs.h1)

html = urlopen(url=url)
bs = BeautifulSoup(html.read(), "html.parser")
print(bs.h1)

bsObj = BeautifulSoup(html.read(), "lxml")
title = bsObj.body.h1
print(title)
