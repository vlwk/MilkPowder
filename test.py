from urllib.request import urlopen
from bs4 import BeautifulSoup

content = read("https://coldstorage.com.sg/fruits-vegetables")

with open("test.txt", "w") as f:
    f.write(content.prettify())
