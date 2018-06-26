import os
import csv

# Path to collect data from the Resources folder
pollData = os.path.join("election_data.csv")

# Set variable to find total voters
total = []
cdates = []
cvotes = []
winner = ["Nobody",0]
clist = []

with open(pollData, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    for row in csvreader:
        total.append(row[2])
    for vote in total:
        if vote not in cdates:
            cdates.append(vote)
    for pers in cdates:
        cvotes.append(total.count(pers))
    for i in range(0, len(cdates)):
        cdict = {"name" : cdates[i], "votes" : cvotes[i]}
        clist.append(cdict)
        if cvotes[i] > winner[1]:
            winner[0] = cdates[i]
            winner[1] = cvotes[i]

totalv = len(total)
print("Election Results")
print("------------------------------")
print(f"Total Votes: {totalv}")
print(cdates[3])

for i in clist:
    print(f'{i["name"]}: {round(100*int(i["votes"])/totalv,2)}% ({i["votes"]})')
#print(clist[1]["name"])
print(len(total))
print(cdates)
print(cvotes)
print(winner[1])
print(winner[0])