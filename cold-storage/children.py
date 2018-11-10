from main import *

file = open("children.csv", "w")

content = read(BASE_URL)
tmp = content.find_all("li", {"class": "col-sm-6 col-md-3 menu-promo"})
for i in tmp[:2]:
    j = i.find_all('a')
    for k in j:
        categories[k['href'][1:]] = k.string.strip()

for x in categories:
    dfs(x)

for x in children:
    file.write(x + "\n")

file.close()
