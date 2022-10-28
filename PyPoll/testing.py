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
old_votes = 0
old_vote = 0
new_votes = 0
poll_result = {}

# Open file with polling data

with open(pollpath) as pollfile:

    # CSV reader specifies delimiter and variable that holds contents

    csvreader = csv.reader(pollfile, delimiter=',')

  # Read the header row first (skip this step if there is now header)

    csv_header = next(csvreader)

    # Read each row of data after the header
    
    for row in csvreader:
        total_count += 1
        current_candidate = str(row[2])

        if previous_candidate == "":
            previous_candidate = current_candidate
            poll_result = {current_candidate : [0]} # New test
            print(poll_result)
            
        if previous_candidate != current_candidate:
            candidate.append(previous_candidate)

            if current_candidate not in poll_result: 
                poll_result[current_candidate] = 1
            
            poll_result[current_candidate] = old_vote + 1 # New test
            previous_candidate = str(row[2])
            candidate_total_votes.append(0)
            c_votes += 1
            new_votes = 0
            # old_votes = poll_result[current_candidate]

        if previous_candidate == current_candidate:
            candidate_total_votes[c_votes] += 1
            # new_votes = old_votes + 1
            poll_result[current_candidate] = new_votes # tally votes for each candidate
            new_votes += 1
            old_vote = [current_candidate]
            print(poll_result)
        previous_candidate = current_candidate

    else:
        candidate.append(current_candidate)

print(poll_result)
# Tally votes for each candidate from each county

for votes in range (0, 9, 3):
    vote_total1 += candidate_total_votes[votes]
    
for votes in range (1, 9, 3):
    vote_total2 += candidate_total_votes[votes]

for votes in range (2, 9, 3):
    vote_total3 += candidate_total_votes[votes]

# Determine winner of election and assign to a variable called winner

winner = ""
if vote_total1 > vote_total2 and vote_total1 > vote_total3:
    winner = candidate[0]
if vote_total2 > vote_total1 and vote_total2 > vote_total3:
    winner = candidate[1]
if vote_total3 > vote_total1 and vote_total3 > vote_total2:
    winner = candidate[2]

# Create output for polling data and print

output = f"""
Election Results
  -------------------------
  Total Votes: {"{:,}".format(total_count)}
  -------------------------
  {candidate[0]}: {round((vote_total1 / total_count),5) * 100}% ({"{:,}".format(vote_total1)})
  {candidate[1]}: {round((vote_total2 / total_count),5) * 100}% ({"{:,}".format(vote_total2)})
  {candidate[2]}: {"{:.3f}".format((vote_total3 / total_count) * 100)}% ({"{:,}".format(vote_total3)})
  -------------------------
  Winner: {winner}
  -------------------------
"""
print(output)

# write the output to a new text file called poll_result.
