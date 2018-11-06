from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

BASE_URL = "https://coldstorage.com.sg/"

visited = []
children = []
categories = {}

def read(url):
    html = urlopen(url)
    content = html.read()
    return BeautifulSoup(content, 'lxml')

def create_file(url):
    new_url = BASE_URL + url
    filename = url + ".txt"
    with open(filename, "w") as f:
        content = read(new_url)
        f.write(content.prettify())
        print(filename + " created successfully!")

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

content = read(BASE_URL)
tmp = content.find_all("li", {"class": "co6l-sm-6 col-md-3 menu-promo"})
for i in tmp[:2]:
    j = i.find_all('a')
    for k in j:
        categories[k['href'][1:]] = k.string.strip()

for x in categories:
    dfs(x)

for y in children:
    ct = read(BASE_URL + y)
    pdts = content.find_all('li',{"class":"col-xs-6 col-sm-4 col-md-3 col-lg-2 open-product-detail algolia-click"})
    for x in pdts2:
        a = x.find('a',{"class":"search product-quick-view"})
        b = x.find('a',{"class":"product-link"})
        c = x.find_all('div',{"class":"content_price"})[0]
        d = c.find('div')
        e = x.find_all('div',{"class":"promo-wrapper"})[0]
        f = e.find_all('span')
        print(a['data-product-size'])
        print("url: "+b['href'])
        print("name: "+b.text)
        print("price: "+d.text)
        if(len(f)>0):
            print("promotion: "+f[0].text)
        print("\n\n")
