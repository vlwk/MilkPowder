from constants import *
from functions import *

from urllib.request import urlopen
from bs4 import BeautifulSoup

content = read(BASE_URL)

tmp = content.find_all("li", {"class": "col-sm-6 col-md-3 menu-promo"})
category_href = []

for i in tmp[:2]:
    j = i.find_all('a')
    for link in j:
        category_href.append(link.get('href')[1:])

print(category_href)

for category in category_href:
    new_url = BASE_URL + category
    filename = category + ".txt"
    with open(filename, "w") as f:
        f.write(read(new_url).prettify())

print("yay")
