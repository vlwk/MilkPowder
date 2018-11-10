from main import *

file = open("coldstorage3.csv", "w")
file.write("name,url,tree,brand,size,price,promotion,\n")

with open("children.csv", "r") as f:
    cutez = csv.reader(f)
    for j in cutez:
        ct = read(BASE_URL + j[0])
        pages = ct.find_all('li', {"class": "page"})
        if len(pages) > 0:
            for i in pages:
                ctt = read(BASE_URL + i.find('a')['href'][1:])
                pdt = ctt.find_all('li', {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-2 open-product-detail algolia-click"})
                for x in pdt:
                    a = x.find('a', {"class": "search product-quick-view"})
                    b = x.find('a', {"class": "product-link"})
                    c = x.find_all('div', {"class": "content_price"})[0]
                    d = c.find_all('div')
                    e = x.find_all('div', {"class":"promo-wrapper"})[0]
                    f = e.find_all('span')
                    tmp = ""
                    if len(d) > 0:
                        tmp = b.text + "," + BASE_URL + b['href'][9:] + "," + j[0] + "," + a['data-product-brand'] + "," + a['data-product-size'][6:] + "," + d[0].text + ","
                    else:
                        tmp = b.text + "," + BASE_URL + b['href'][9:] + "," + j[0] + "," + a['data-product-brand'] + "," + a['data-product-size'][6:] + "," + "" + ","
                    if len(f) > 0:
                        tmp += f[0].text
                    tmp += "\n"
                    print(tmp)
                    file.write(tmp)
        else:
            pdt = ct.find_all('li', {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-2 open-product-detail algolia-click"})
            for x in pdt:
                a = x.find('a', {"class": "search product-quick-view"})
                b = x.find('a', {"class": "product-link"})
                c = x.find_all('div', {"class": "content_price"})[0]
                d = c.find_all('div')
                e = x.find_all('div', {"class":"promo-wrapper"})[0]
                f = e.find_all('span')
                tmp = ""
                if len(d) > 0:
                    tmp = b.text + "," + BASE_URL + b['href'][9:] + "," + j[0] + "," + a['data-product-brand'] + "," + a['data-product-size'][6:] + "," + d[0].text + ","
                else:
                    tmp = b.text + "," + BASE_URL + b['href'][9:] + "," + j[0] + "," + a['data-product-brand'] + "," + a['data-product-size'][6:] + "," + "" + ","
                if len(f) > 0:
                    tmp += f[0].text
                tmp += "\n"
                print(tmp)
                file.write(tmp)
file.close()
