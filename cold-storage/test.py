from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

def read(url):
    html = urlopen(url)
    content = html.read()
    return BeautifulSoup(content, 'lxml')

BASE_URL = "https://coldstorage.com.sg/"

content = read(BASE_URL + "fruits-vegetables/fresh-fruits/apples-pears")
pdts = content.find_all('a', {"class": "product-link"})
for i in pdts:
    print(i)
