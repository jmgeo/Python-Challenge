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

    #time to calculate. Operation should return the percentage of votes for each candidate as requested.
    for item in vote_tally:
        winner = format(((item[0][1])*100/sum(candidate_count.values())), '.3f')
        second = format(((item[1][1])*100/sum(candidate_count.values())), '.3f')
        third = format(((item[2][1])*100/sum(candidate_count.values())), '.3f')
        fourth = format(((item[3][1])*100/sum(candidate_count.values())), '.3f')

#print all this jazz to the gitbash terminal
print("Election Results")
print("___________________________________")
print(f"Total Votes: {sum(candidate_count.values())}")
print("___________________________________")
print(f"{vote_tally[0][0][0]}: {winner}% ({vote_tally[0][0][1]})")
print(f"{vote_tally[0][1][0]}: {second}% ({vote_tally[0][1][1]})")
print(f"{vote_tally[0][2][0]}: {third}% ({vote_tally[0][2][1]})")
print(f"{vote_tally[0][3][0]}: {fourth}% ({vote_tally[0][3][1]})")
print("___________________________________")
print(f"Winner: {vote_tally[0][0][0]}")
print("___________________________________")

#export the results of the script into a text file

analysis_file = os.path.join("Analysis", "analysis.txt")

#pretty much the same setup as the PyBank output
with open(analysis_file, "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("___________________________________\n")
    outfile.write(f"Total Votes: {sum(candidate_count.values())}\n")
    outfile.write("___________________________________\n")
    outfile.write(f"{vote_tally[0][0][0]}: {winner}% ({vote_tally[0][0][1]})\n")
    outfile.write(f"{vote_tally[0][1][0]}: {second}% ({vote_tally[0][1][1]})\n")
    outfile.write(f"{vote_tally[0][2][0]}: {third}% ({vote_tally[0][2][1]})\n")
    outfile.write(f"{vote_tally[0][3][0]}: {fourth}% ({vote_tally[0][3][1]})\n")
    outfile.write("___________________________________\n")
    outfile.write(f"Winner: {vote_tally[0][0][0]}\n")
    outfile.write("___________________________________\n")
    


