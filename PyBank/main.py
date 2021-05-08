#import the dependencies
import os
import csv

#define needed variables to perform the homework
months = []
PnL = []

#set the needed counts equal to zero to start
total_months = 0
total_PnL = 0
last_month_PnL = 0
this_month_PnL = 0
PnL_change = 0

#change the directory to the file location
csvpath = os.path.join("Resources", "budget_data.csv")

#open the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    print(f"CSV Header: {csvheader}")

    for row in csvreader:
        #count the total number of months
        total_months +=1

        #count the total P&L
        this_month_PnL = int(row[1])
        total_PnL += this_month_PnL