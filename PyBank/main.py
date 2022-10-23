#  Task is to create a Python script that analyzes the records to calculate each of the following:
#
#   * The total number of months included in the dataset
#
#   * The net total amount of "Profit/Losses" over the entire period
#
#   * The changes in "Profit/Losses" over the entire period, and then the average of those changes
#
#   * The greatest increase in profits (date and amount) over the entire period
#
#   * The greatest decrease in profits (date and amount) over the entire period

# Input modules needed for the Challenge

import os, csv

# create path and open file for reading
bankpath = "Resources/budget_data.csv"
outputpath = 'analysis/finance_result.txt'
# bankpath = os.path.join('Resources', 'budget_data.csv')
#print(bankpath)

total_month = 0
total_profit = 0
previous_profit = 0
total_change = 0
month_change = 0
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""

# Open the CSV File

with open(bankpath) as bankfile:

    # CSV reader specifies delimiter and variable that holds contents

    csvreader = csv.reader(bankfile, delimiter=',')
    print(csvreader)

    # Read the header row first (skip this step if there is now header)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header

    for row in csvreader:
        # print(row)
        # new way
        total_month += 1
        total_profit = total_profit + int(row[1])
        current_profit = int(row[1])
        change = 0

        if previous_profit != 0:
            change = current_profit - previous_profit
            total_change = total_change + change
            month_change += 1

        previous_profit = current_profit

        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_date = row[0]

        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = row[0]

# print(month_change)





# Create variables needed
# list of months, profit_loss, month_count, net_profit, profit_change, profit_mean, percent_up, percent_down

#print (str(row[0]))
# print (str(row[0]))
#print (str(row[1]))
#print (str(row[2]))
#print (str(row[3]))

output = f"""
Financial Analysis
----------------------------
Total Months: {total_month}
Total: ${total_profit:,}
Average Change: ${total_change / month_change:,.2f}
Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase:,})
Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease:,})
"""

print(output)

with open(outputpath, "w") as f:
    f.write(output)