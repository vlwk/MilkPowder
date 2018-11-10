import csv
import random

cnt = 0

yay = ""

with open("coldstorage2.csv", "r") as f:
    file = csv.reader(f)
    for line in file:
        if (cnt == 0):
            cnt += 1
            continue

        itemName = line[0].rstrip()
        iuid = cnt + 29
        istock = random.randint(0,100)
        shelfLocation = "shelf" + str(random.randint(1, 4))
        shelfRow = random.randint(1, 4)
        shelfColumn = random.randint(1, 10)
        friendlyLocation = line[2].rstrip()
        cnt += 1

        arr = []
        a = line[0].rstrip().split(" ")
        b = line[2].rstrip().split('/')
        for c in b:
            d = c.split('-')
            for i in d:
                if i not in arr:
                    arr.append(i)
        for i in a:
            if i not in arr:
                arr.append(i)
        tags = "["
        for i in arr:
            tags += ("\"" + i + "\"")
            tags += ","
        tags = tags[:len(tags)-1]

        tags += "]"

        sleep = "{"
        sleep += ("\"iuid\":" + str(iuid) + ",")
        sleep += ("\"istock\":" + str(istock) + ",")
        sleep += ("\"itemName\":" + "\"" + itemName + "\"" + ",")
        sleep += ("\"shelfLocation\":" + "\"" + shelfLocation + "\"" + ",")
        sleep += ("\"friendlyLocation\":" + "\"" + friendlyLocation + "\"" + ",")
        sleep += ("\"shelfRow\":" + str(shelfRow) + ",")
        sleep += ("\"shelfColumn\":" + str(shelfColumn) + ",")
        sleep += ("\"tags\":" + tags)
        sleep += "},\n"
        yay += sleep

with open("plswork.txt", "w") as f:
    f.write(yay)
