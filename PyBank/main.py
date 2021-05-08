#import the dependencies
import os
import csv

#define needed variables to perform the homework
months = []
P&L = []

#set the needed counts equal to zero to start
total_months = 0
total_PnL = 0
average_change_PnL = 0
greatest_inc_P = 0
greatest_dec_L = 0

#change the directory to the file location
csvpath = os.path.join("Resources", "budget_data.csv")

#open the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    print(f"CSV Header: {csvheader}")

#the number of months in the spreadsheet is simply equal to the number of rows not including the header
    #months = len(list(csvreader))
    #print (months)

#the total of the Profits and Losses is equal to the sum of all the values in the second column of the csv not including the header
    







