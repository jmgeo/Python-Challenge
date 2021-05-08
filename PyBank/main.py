import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

#csv_file = csv.reader(open("csvpath"))

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    print(f"CSV Header: {csvheader}")

for Date in csvfile:
    print (Date)


#dist = 0
#for row in csv_file:
    #_dist = row[2]


