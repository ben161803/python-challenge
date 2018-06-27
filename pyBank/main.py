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
        # set variable for profits/losses
        rev = int(row[1])
        # add each month to a list
        months.append(row[0])
        # add each month's profit/loss to a list
        profits.append(rev)
        # if the profits of this month are larger than largestp set new values for largestp
        if rev > largestp[1]:
            largestp[0] = row[0]
            largestp[1] = rev
        # if the losses of this month are greater than largestl set new values for largestl 
        if rev < largestl[1]:
            largestl[0] = row[0]
            largestl[1] = rev
    # count number of months
    amount = int(len(months))
    # the 1st month's profits
    first = profits[0]
    # last month's profits
    last = profits[amount-1]
    # sum all profits
    total = sum(profits)
    # calculate average month to month change
    change = round((last-first)/(amount-1),2)

    print("Financial Analysis")
    print("------------------------------")
    print(f"Total Months: {amount}")
    print(f"Total Profit/Losses: ${total}")
    print(f"Average Change: ${change}")
    print(f"Greatest Increase in Profits: {largestp[0]} (${largestp[1]})")
    print(f"Greatest Decrease in Profits: {largestl[0]} (${largestl[1]})")

    f = open('main.txt','a')
    f.write("\n" + "Financial Analysis")
    f.write("\n" + "------------------------------")
    f.write('\n' + f"Total Months: {amount}")
    f.write('\n' + f"Total Profit/Losses: ${total}")
    f.write('\n' + f"Average Change: ${change}")
    f.write('\n' + f"Greatest Increase in Profits: {largestp[0]} (${largestp[1]})")
    f.write('\n' + f"Greatest Decrease in Profits: {largestl[0]} (${largestl[1]})")
    f.close()