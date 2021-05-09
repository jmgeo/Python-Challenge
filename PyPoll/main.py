#import the dependencies
import os
import csv

#define needed variables to perform the homework
#months = []
#PnL = []

#set the needed counts equal to zero to start
#total_months = 0
#total_PnL = 0
#last_month_PnL = 0
#this_month_PnL = 0
#PnL_change = 0

#change the directory to the file location
#csvpath = os.path.join("Resources", "budget_data.csv")

#open the csv file
#with open(csvpath) as csvfile:
    #csvreader = csv.reader(csvfile, delimiter=',')
    #csvheader = next(csvreader)
    #print(f"CSV Header: {csvheader}")

    #for row in csvreader:
        #count the total number of months
        #total_months +=1

        #count the total P&L
        #this_month_PnL = int(row[1])
        #total_PnL += this_month_PnL

        #if (total_months ==1):
            #make the last month P&L equal to the value of this month's P&L
            #last_month_PnL = this_month_PnL
            #continue

        #else:
            #calculate the P&L
            #PnL_change = this_month_PnL - last_month_PnL

            #append to the months
            #months.append(row[0])

            #append to P&L
            #PnL.append(PnL_change)

            #set the current month P&L to the previous and continue the loop
            #last_month_PnL = this_month_PnL
    
    #calculate the sum and the average P&L over the dataset timeframe, as well as the max and min P&Ls
    #sum_PnL = sum(PnL)
    #ave_PnL = round(sum_PnL/(total_months -1),2)
    #max_change_PnL = max(PnL)
    #min_change_PnL = min(PnL)

    #find the index of the maximum and minimum changes in values for the P&Ls for the dataset timeframe
    #max_month_index = PnL.index(max_change_PnL)
    #min_month_index = PnL.index(min_change_PnL)

    #find the value for the highest and lowest performing months
    #high_month = months[max_month_index]
    #low_month = months[min_month_index]

#print all this jazz to the gitbash terminal
#print("Financial Analysis")
#print("___________________________________")
#print(f"Total Months: {total_months}")
#print(f"Total: ${total_PnL}")
#print(f"Average Change: {ave_PnL}")
#print(f"Greatest Increase in Profits: {high_month} (${max_change_PnL})")
#print(f"Greatest Decrease in Losses: {low_month} (${min_change_PnL})")

#export the results of the script into a text file

#analysis_file = os.path.join("Analysis", "analysis.txt")
#with open(analysis_file, "w") as outfile:
    #outfile.write("Financial Analysis\n")
    #outfile.write("___________________________________\n")
    #outfile.write(f"Total Months: {total_months}\n")
    #outfile.write(f"Total: ${total_PnL}\n")
    #outfile.write(f"Average Change: {ave_PnL}\n")
    #outfile.write(f"Greatest Increase in Profits: {high_month} (${max_change_PnL})\n")
    #outfile.write(f"Greatest Decrease in Losses: {low_month} (${min_change_PnL})\n")

