import csv

with open('children.csv', 'r') as f:
    reader = csv.reader(f)
    for i in reader:
        print(i[0])
