from urllib.request import urlopen
from bs4 import BeautifulSoup

def read(url):
    html = urlopen(url)
    content = html.read()
    return BeautifulSoup(content, 'html.parser')
