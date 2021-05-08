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

        if (total_months ==1):
            #make the last month P&L equal to the value of this month's P&L
            last_month_PnL = this_month_PnL
            continue

        else:
            #calculate the P&L
            PnL_change = this_month_PnL - last_month_PnL

            #append to the months
            months.append(row[0])

            #append to P&L
            PnL.append(PnL_change)

            #set the current month P&L to the previous and continue the loop
            last_month_PnL = this_month_PnL
    
    #calculate the sum and the average P&L over the dataset timeframe, as well as the max and min P&Ls
    sum_PnL = sum(PnL)
    ave_PnL = round(sum_PnL/(total_months -1),2)
    max_change_PnL = max(PnL)
    min_change_PnL = min(PnL)

    
