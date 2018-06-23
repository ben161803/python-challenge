import os
import csv

# Path to collect data from the Resources folder
budgetData = os.path.join("Resources", "budget_data.csv")

# List of months
months = []

# each months profits
profits = []

# change in profits
first = 0
last = 0

# find highest profits and losses
largestp = ["month", 0]
largestl = ["month", 0]

with open(budgetData, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    for row in csvreader:
        rev = int(row[1])
        months.append(row[0])
        profits.append(rev)
        if rev > largestp[1]:
            largestp[0] = row[0]
            largestp[1] = rev
        if rev < largestl[1]:
            largestl[0] = row[0]
            largestl[1] = rev
    amount = int(len(months))
    first = profits[0]
    last = profits[amount-1]
    total = sum(profits)
    change = round((last-first)/(amount-1),2)
    print(amount)
    print(total)
    print(change)
    print(largestp)
    print(largestl)