#import the dependencies
import os
import csv
import collections
from collections import Counter

#define needed variables to perform the homework
#months = []
#PnL = []
candidates = []
vote_tally = []

#change the directory to the file location
csvpath = os.path.join("Resources", "election_data.csv")

#open the csv file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvfile)
    print(f"CSV Header: {csvheader}")

    for row in csvreader:
        #append the votes for each candidate to the appropriate row
        candidates.append(row[2])
    
    #sort the list of candidates by ascending order
    candidates_list = sorted(candidates)

    #rearrange the sorted list of candidates by the most prevalent result
    arranged_list = candidates_list

    #tally the votes for each candidate in the order of prevalanece and append it to the list
    candidate_count = Counter(arranged_list)
    vote_tally.append(candidate_count.most_common())
        
    
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

