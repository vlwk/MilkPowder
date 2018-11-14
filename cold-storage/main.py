from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import os

BASE_URL = "https://coldstorage.com.sg/"

visited = []
children = []
categories = {}

def read(url):
    html = urlopen(url)
    content = html.read()
    return BeautifulSoup(content, 'lxml')


def dfs(node):
    url = BASE_URL + node
    if node in visited:
        return
    visited.append(node)
    content = read(url)
    print("processing: " + node)
    sub_categories = content.find_all('a', {"class": "subcat_catalog"})
    if len(sub_categories) == 0:
        children.append(node)
        print("appended: " + node)
        return
    for x in sub_categories:
        nd = x['href'][1:]
        dfs(nd)
