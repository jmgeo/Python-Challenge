import os
import csv

with open(csv)

csvpath = os.path.join("..", "Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)

