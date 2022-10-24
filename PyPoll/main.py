# Module 3 Challenge -- Python
# Vincent Passanisi, Due October 31, 2022

# Import necessary modules

import os, csv

# Create path for resources and output

pollpath = "Resources/election_data.csv"
poll_output = 'analysis/poll_result.txt'

# Create global variables

total_count = 0
candidates_all = ""
candidate = []
previous_candidate = ""
candidate_total_votes = []
candidate_total_votes.append(0)
c_votes = 0

# Open file with polling data

with open(pollpath) as pollfile:

    # CSV reader specifies delimiter and variable that holds contents

    csvreader = csv.reader(pollfile, delimiter=',')
    print(csvreader)

  # Read the header row first (skip this step if there is now header)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    print(candidate_total_votes[0])
    exit
    for row in csvreader:
        # print(row)
        # break
        total_count += 1
        candidates_all = str(row[2])
        
        if previous_candidate != "" and previous_candidate != candidates_all:
            candidate.append(previous_candidate)
            previous_candidate = str(row[2])
            # candidate_total_votes += 1             

        previous_candidate = candidates_all

        # candidate_total_votes[row(0)] += 1
        print (previous_candidate)
                           

# Create output for subroutine

output = f"""
Election Results
  -------------------------
  Total Votes: {total_count}
  -------------------------
  {candidate[0]}: 23.049% (85213)
  {candidate[1]}: 73.812% (272892)
  {candidate[2]}: 3.139% (11606)
  -------------------------
  Winner: Diana DeGette
  -------------------------
"""
print(output)