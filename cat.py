from bs4 import BeautifulSoup

with open("categories/fruits-vegetables.txt", "r") as f:
    content = BeautifulSoup(f.read())
    print(content.find_all('a'))
