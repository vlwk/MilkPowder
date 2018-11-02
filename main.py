from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

BASE_URL = "https://coldstorage.com.sg/"

def read(url): # uses lxml parser
    html = urlopen(url)
    content = html.read()
    return BeautifulSoup(content, 'lxml')

def extract_categories_to_dict():
    dict = {}
    content = read(BASE_URL)
    tmp = content.find_all("li", {"class": "col-sm-6 col-md-3 menu-promo"})
    for i in tmp[:2]:
        j = i.find_all('a')
        for k in j:
            dict[k['href'][1:]] = k.string.strip()
    return dict

def create_files(dict):
    for category in dict:
        new_url = BASE_URL + category
        filename = category + ".txt"
        with open(filename, "w") as f:
            content = read(new_url)
            f.write(content.prettify())
            print(filename + " created successfully")

def create_directories(dict):
    for category in dict:
        os.mkdir(category)

def extract_subcategories_to_dict():
    dict = {}
    with open("fruits-vegetables.txt", "r") as f:
        content = BeautifulSoup(f.read(), 'lxml')
        tmp2 = content.find_all('div', {"class": "layer-content"})
        # tmp2 = content.find_all('a', {"class": "static"})
        for i in tmp2[1:]:
            j = i.find_all('a')
            for k in j:
                dict[k['href'][1:]] = k.string.strip()
    return dict

categories = extract_categories_to_dict() # dictionary (link, category)
create_files(categories)
sub_categories = extract_subcategories_to_dict() # dictionary (link, category)
create_directories(categories)
create_files(sub_categories)
