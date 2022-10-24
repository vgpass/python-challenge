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
candidate = []
previous_candidate = ""
candidate_total_votes = []
candidate_total_votes.append(0)
votes = 0
c_votes = 0
vote_total1 = 0
vote_total2 = 0
vote_total3 = 0

# Open file with polling data

with open(pollpath) as pollfile:

    # CSV reader specifies delimiter and variable that holds contents

    csvreader = csv.reader(pollfile, delimiter=',')
    print(csvreader)

  # Read the header row first (skip this step if there is now header)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        # print(row)
        # break
        total_count += 1
        current_candidate = str(row[2])

        if previous_candidate == "":
            previous_candidate = current_candidate

        if previous_candidate != current_candidate:
            candidate.append(previous_candidate)
            previous_candidate = str(row[2])
            candidate_total_votes.append(0)
            c_votes += 1

        if previous_candidate == current_candidate:
            candidate_total_votes[c_votes] += 1
            # print (candidate_total_votes[c_votes])
        previous_candidate = current_candidate

    else:
        candidate.append(current_candidate)

        # candidate_total_votes[row(0)] += 1

# Tally votes for each candidate from each county

for votes in range (0, 8, 3):
    vote_total1 += candidate_total_votes[votes]
    
for votes in range (1, 8, 3):
    vote_total2 += candidate_total_votes[votes]

for votes in range (2, 8, 3):
    vote_total3 += candidate_total_votes[votes]

# Determine % of total vote that each candidate received

# Create output for polling data and print

output = f"""
Election Results
  -------------------------
  Total Votes: {total_count}
  -------------------------
  {candidate[0]}: {(vote_total1 / total_count) * 100}% ({vote_total1})
  {candidate[1]}: {(vote_total2 / total_count * 100)}% ({vote_total2})
  {candidate[2]}: {(vote_total3 / total_count * 100)}% ({vote_total3})
  -------------------------
  Winner: Diana DeGette
  -------------------------
"""
print(output)