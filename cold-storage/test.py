from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

def read(url):
    html = urlopen(url)
    content = html.read()
    return BeautifulSoup(content, 'lxml')

BASE_URL = "https://coldstorage.com.sg/"

content = read(BASE_URL + "fruits-vegetables/fresh-fruits/apples-pears")

pdts2=content.find_all('li',{"class":"col-xs-6 col-sm-4 col-md-3 col-lg-2 open-product-detail algolia-click"})

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
