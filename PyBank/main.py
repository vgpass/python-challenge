# Python Bank Challenge
# Vincent Passanisi
# October 2022 
# 
# Task is to create a Python script that analyzes the records to calculate each of the following:
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
bankoutput = 'analysis/finance_result.txt'

# Note: other way to create path: bankpath = os.path.join('Resources', 'budget_data.csv')

# Create global variables needed for sub-routine 

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

    # Read the header row first (skip this step if there is now header)

    csv_header = next(csvreader)

    # Read each row of data after the header
    # row[0] is month
    # row[1] is profit
    # Increment total_month by one to get a count of how many months in data set.
    # Sum total_profit by adding the profit of each row to the previous sum.
    # Set current_profit to the profit of the current row

    for row in csvreader: 
        total_month += 1
        total_profit = total_profit + int(row[1])
        current_profit = int(row[1])
        change = 0

        # If previous profit is equal to 0, then set previous_profit to current_profit
        # Otherwise the change variable is set to the difference bewteen profit in the current month and profit in the previous month.
        # total_chamge is set to accumulate the total change over the entire data set
        # create counter month_change for calculating mean change over the data set.

        if previous_profit != 0:
            change = current_profit - previous_profit
            total_change = total_change + change
            month_change += 1

        previous_profit = current_profit

        # Determine if the current change is greater than the previous change
        # If so, greatest_increase becomes the new change, and set greatest_increase_date to the current date.
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_date = row[0]

        # Determine if the current change is less than the previous change
        # If so, greatest_decrease becomes the new change, and set greatest_decrease_date to the current date.
        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = row[0]

# list of months, profit_loss, month_count, net_profit, profit_change, profit_mean, percent_up, percent_down
# Format output for printing
output = f"""
Financial Analysis
----------------------------
Total Months: {total_month}
Total: ${total_profit:,}
Average Change: ${total_change / month_change:,.2f}
Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase:,})
Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease:,})
"""

# print the output to the screen
print(output)

# write the output to a new text file called finance_result.
with open(bankoutput, "w") as f:
    f.write(output)