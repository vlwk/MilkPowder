import csv

cnt = 0

wow = open("tags.csv", "w")
writer = csv.writer(wow)

with open("coldstorage2.csv", "r") as f:
    file = csv.reader(f)
    for line in file:
        if (cnt == 0):
            cnt = 1
            continue
        arr = []
        a = line[0].rstrip().split(" ") # name
        b = line[2].rstrip().split('/') # tree
        for c in b:
            d = c.split('-')
            for i in d:
                if i not in arr:
                    arr.append(i)
        for i in a:
            if i not in arr:
                arr.append(i)
        tmp = ""
        for i in arr:
            tmp += i
            tmp += ","
        tmp = tmp[:len(tmp)-1]
        row = []
        row.append(line[0].rstrip())
        row.append(tmp)
        print(row)
        writer.writerow(row)
        cnt += 1

wow.close()
