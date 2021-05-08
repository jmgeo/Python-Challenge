import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

#csv_file = csv.reader(open("csvpath"))

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    print(f"CSV Header: {csvheader}")

    #for row in csvfile:
        #print (row)

    months = len(list(csvreader))
    print (months)


#dist = 0
#for row in csv_file:
    #_dist = row[2]


