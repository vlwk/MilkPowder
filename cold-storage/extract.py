from main import *

file = open("coldstorage3.csv", "w")
file.write("name,url,tree,brand,size,price,promotion,tags,\n")
filez = csv.writer(file)

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
                    row = []
                    row.append(b.text)
                    row.append(BASE_URL + b['href'][9:])
                    row.append(j[0])
                    row.append(a['data-product-brand'])
                    row.append(a['data-product-size'][6:])
                    if len(d) > 0:
                        row.append(d[0].text)
                    else:
                        row.append("")
                    if len(f) > 0:
                        row.append(f[0].text)
                    else:
                        row.append("")
                    arr = []
                    aa = b.text.rstrip().split(" ")
                    bb = b['href'][9:].rstrip().split("/")
                    for cc in bb:
                        dd = cc.split('-')
                        for i in dd:
                            if i not in arr:
                                arr.append(i)
                    for i in aa:
                        if i not in arr:
                            arr.append(i)
                    foo = ""
                    for i in arr:
                        foo += i
                        foo += ","
                    foo = foo[:len(foo)-1]
                    print(foo)
                    row.append(foo)
                    print(row)
                    filez.writerow(row)
        else:
            pdt = ct.find_all('li', {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-2 open-product-detail algolia-click"})
            for x in pdt:
                a = x.find('a', {"class": "search product-quick-view"})
                b = x.find('a', {"class": "product-link"})
                c = x.find_all('div', {"class": "content_price"})[0]
                d = c.find_all('div')
                e = x.find_all('div', {"class":"promo-wrapper"})[0]
                f = e.find_all('span')
                row = []
                row.append(b.text)
                row.append(BASE_URL + b['href'][9:])
                row.append(j[0])
                row.append(a['data-product-brand'])
                row.append(a['data-product-size'][6:])
                if len(d) > 0:
                    row.append(d[0].text)
                else:
                    row.append("")
                if len(f) > 0:
                    row.append(f[0].text)
                else:
                    row.append("")
                arr = []
                aa = b.text.rstrip().split(" ")
                bb = b['href'][9:].rstrip().split("/")
                for cc in bb:
                    dd = cc.split('-')
                    for i in dd:
                        if i not in arr:
                            arr.append(i)
                for i in aa:
                    if i not in arr:
                        arr.append(i)
                foo = ""
                for i in arr:
                    foo += i
                    foo += ","
                foo = foo[:len(foo)-1]
                print(foo)
                row.append(foo)
                print(row)
                filez.writerow(row)
file.close()
