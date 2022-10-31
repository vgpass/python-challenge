# Module 3 Challenge -- Python Poll Challenge
# Vincent Passanisi, Due October 31, 2022

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
candidate = []
previous_candidate = ""
new_votes = 1
poll_result = {}

# Open file with polling data

with open(pollpath) as pollfile:

    # CSV reader specifies delimiter and variable that holds contents

    csvreader = csv.reader(pollfile, delimiter=',')

  # Read the header row first (skip this step if there is now header)

    csv_header = next(csvreader)

    # Read each row of data after the header
    
    for row in csvreader:
        total_count += 1 # Tally the total vote count for the election
        current_candidate = str(row[2])
        current_county = str(row[1])

        if previous_candidate == "":
            previous_candidate = current_candidate # First iteration of loop only
            previous_county = current_county
            poll_result = {current_county : {current_candidate : [1]}} # New test
            # print(poll_result)
                      
        if previous_candidate != current_candidate and previous_county == current_county:
            poll_result[current_county][current_candidate] = 1
            previous_candidate = str(row[2])
            new_votes = 1

        if previous_candidate != current_candidate and previous_county != current_county:
            # candidate.append(previous_candidate)
            poll_result.__setitem__(current_county, {current_candidate :1})
            poll_result[current_county][current_candidate] = 1
            previous_candidate = str(row[2])
            new_votes = 1


        if previous_candidate == current_candidate:
            poll_result[current_county][current_candidate] = new_votes # tally votes for each candidate
            new_votes += 1

        previous_candidate = current_candidate
        previous_county = current_county

    # else:
        # candidate.append(current_candidate)

# Looping to access values in nested dictionaries to total the votes that each candidate received
# in each county and assign those totals to a new dictionary called candidate_dict.
# Special thank you to my tutor, Saad Khan, for helping me with the logic of this after 2 days of frustration!
# I would not have been able to figure this out on my own.

candidate_dict = {}
candidate_list = []
for k, v in poll_result.items():
    for x, y in v.items():
        if x not in candidate_list:
            candidate_list.append(x)
            candidate_dict[x]=0
        candidate_dict[x]+=y

total = sum(candidate_dict.values())
result = {key: (value / total) * 100 for key, value in candidate_dict.items()}

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
  {candidate_list[0]}: {round(result[candidate_list[0]],2)}% ({"{:,}".format(candidate_dict[candidate_list[0]])})
  {candidate_list[1]}: {round(result[candidate_list[1]],2)}% ({"{:,}".format(candidate_dict[candidate_list[1]])})
  {candidate_list[2]}: {round(result[candidate_list[2]],2)}% ({"{:,}".format(candidate_dict[candidate_list[2]])})
  -------------------------
  Winner: {winner}
  -------------------------
"""
print(output)

# write the output to a new text file called poll_result.
with open(poll_output, "w") as f:
    f.write(output)