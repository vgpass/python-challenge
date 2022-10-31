# Module 3 Challenge -- Python Poll Challenge
# Vincent Passanisi, Due October 31, 2022
# VERSION 2

# I wasn't happy with my first attempt. This version creates a nested dictionary with all values from the election.
# The nested dictionary has the following structure:
#       County 1: Candidate 1: Vote Total
#                 Candidate 2: Vote Total
#                 Candidate 3: Vote Total
#       County 2: Candidate 1: Vote Total
#                 Candidate 2: Vote Total
#                 Candidate 3: Vote Total
#       County 3: Candidate 1: Vote Total
#                 Candidate 2: Vote Total
#                 Candidate 3: Vote Total

# Import necessary modules

import os, csv

# Create path for resources and output

pollpath = "Resources/election_data.csv"
poll_output = "analysis/poll_result.txt"

# Create global variables

total_count = 0
current_candidate = ""
current_county = ""
previous_county = ""
previous_candidate = ""
new_votes = 1
poll_result = {}        # This variable is the nested dictionary that will hold all values.

# Open file with polling data

with open(pollpath) as pollfile:

    # CSV reader specifies delimiter and variable that holds contents

    csvreader = csv.reader(pollfile, delimiter=',')

  # Read the header row first (skip this step if there is now header)

    csv_header = next(csvreader)

    # Read each row of data after the header
    
    for row in csvreader:
        total_count += 1                    # Tally the total vote count for the election
        current_candidate = str(row[2])     # Assign variables for current row
        current_county = str(row[1])

        if previous_candidate == "":                    # First iteration of loop only
            previous_candidate = current_candidate 
            previous_county = current_county
            poll_result = {current_county : {current_candidate : [1]}} # poll_result is the nested dictionary that will hold all values.
                      
        if previous_candidate != current_candidate and previous_county == current_county: # Conditional to count votes within a county
            poll_result[current_county][current_candidate] = 1
            previous_candidate = str(row[2])
            new_votes = 1

        if previous_candidate != current_candidate and previous_county != current_county: # Conditional to append a new county when the county has changed.
            poll_result.__setitem__(current_county, {current_candidate :1}) # Creates key for new county
            poll_result[current_county][current_candidate] = 1              # Creates new candidate in the county and starts the vote count.
            previous_candidate = str(row[2])                                # Sets the variable to the current row for later comparison.
            new_votes = 1


        if previous_candidate == current_candidate:                     # Continue vote count when there is no change in the candidate name.
            poll_result[current_county][current_candidate] = new_votes  # Tally votes for each candidate
            new_votes += 1                                              # Increase the tally by 1 vote.

        previous_candidate = current_candidate                          # Update the variables for comparison.
        previous_county = current_county

    # else:
        # candidate.append(current_candidate)

# Looping to access values in nested dictionaries to total the votes that each candidate received
# in each county and assign those totals to a new dictionary called candidate_dict.
# Special thank you to my tutor, Saad Khan, for helping me with the logic of this after 2 days of frustration!
# I would not have been able to figure this out on my own.

candidate_dict = {}                     # create new dictionary to tally votes for each candidate in each county.
candidate_list = []                     # create new list to hold candidate names.
for k, v in poll_result.items():        # Loop through dictionary to access nested values.
    for x, y in v.items():              # Loop through keys in nested dictionaries. 
        if x not in candidate_list:     # Determines if the candidate is already in the list to avoid an error.
            candidate_list.append(x)    # Appends new candidate to the list if the name isn't already in the list.
            candidate_dict[x]=0         # Assignes a value of zero on the first iteration of the loop.
        candidate_dict[x]+=y            # Adds the county totals to each other for each candidate.

total = sum(candidate_dict.values()) # Totals the votes for all candidates. There is a second variable called total_count that does the same thing.
result = {key: (value / total) * 100 for key, value in candidate_dict.items()} # Loop conditional to calculate the % of total vote that each candidate earned. 

# Use conditional statements to determine which candidate has the most votes.
# Assign the name of the candidate with the most votes to a variable "winner."

winner = ""
if candidate_dict[candidate_list[0]] > candidate_dict[candidate_list[1]] and candidate_dict[candidate_list[0]] > candidate_dict[candidate_list[2]]:
     winner = candidate_list[0]
if candidate_dict[candidate_list[1]] > candidate_dict[candidate_list[0]] and candidate_dict[candidate_list[1]] > candidate_dict[candidate_list[2]]:
     winner = candidate_list[1]
if candidate_dict[candidate_list[2]] > candidate_dict[candidate_list[0]] and candidate_dict[candidate_list[2]] > candidate_dict[candidate_list[1]]:
     winner = candidate_list[2]

# Create output for polling data and print

output = f"""
Election Results
  -------------------------
  Total Votes: {"{:,}".format(total_count)}
  -------------------------
  {candidate_list[0]}: {round(result[candidate_list[0]],3)}% ({"{:,}".format(candidate_dict[candidate_list[0]])})
  {candidate_list[1]}: {round(result[candidate_list[1]],3)}% ({"{:,}".format(candidate_dict[candidate_list[1]])})
  {candidate_list[2]}: {round(result[candidate_list[2]],3)}% ({"{:,}".format(candidate_dict[candidate_list[2]])})
  -------------------------
  Winner: {winner}
  -------------------------
"""
print(output)

# write the output to a new text file called poll_result.
with open(poll_output, "w") as f:
    f.write(output)