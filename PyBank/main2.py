import os
import csv
import functools

csvpath = os.path.join("Resources", "budget_data.csv")

#csv_file = csv.reader(open("csvpath"))

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    print(f"CSV Header: {csvheader}")

with open(csvfile) as fin:
    headerline = fin.next()
    total = 0
    for row in csv.reader(fin):
        total += int(row[1])
    print (total)