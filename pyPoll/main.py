import os
import csv

# Path to collect data from the Resources folder
pollData = os.path.join("election_data.csv")

# Set list of votes
total = []
# Set list of vote getters
cdates = []
# Set list of amount of votes per candidate
cvotes = []
# Set list for winner and number of votes
winner = ["Nobody",0]
# Set list of dictionaries (name and number of votes)
clist = []

with open(pollData, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    for row in csvreader:
        # Add vote to list
        total.append(row[2])
    # For each vote in the list add the candidate to cdates if candidate is not in cdates
    for vote in total:
        if vote not in cdates:
            cdates.append(vote)
    # For each candidate count votes in total
    for pers in cdates:
        cvotes.append(total.count(pers))
    # Combine cdates and cvotes into list of dictionaries
    for i in range(0, len(cdates)):
        cdict = {"name" : cdates[i], "votes" : cvotes[i]}
        clist.append(cdict)
        # If current candidate has more votes than previous "winner" then rewrite "winner"
        if cvotes[i] > winner[1]:
            winner[0] = cdates[i]
            winner[1] = cvotes[i]

totalv = len(total)
print("Election Results")
print("------------------------------")
print(f"Total Votes: {totalv}")
for i in clist:
    print(f'{i["name"]}: {round(100*int(i["votes"])/totalv,2)}% ({i["votes"]})')
print("------------------------------")
print(f"Winner: {winner[0]}")
print("------------------------------")

f = open('main.txt','a')
f.write("\n" + "Election Results")
f.write('\n' + "------------------------------")
f.write('\n' + f"Total Votes: {totalv}")
for i in clist:
    f.write('\n' + f'{i["name"]}: {round(100*int(i["votes"])/totalv,2)}% ({i["votes"]})')
f.write('\n' + "------------------------------")
f.write('\n' + f"Winner: {winner[0]}")
f.write('\n' + "------------------------------")