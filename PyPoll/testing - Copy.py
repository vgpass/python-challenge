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
        total_count += 1 # Tally the total vote count for the election
        current_candidate = str(row[2])
        current_county = str(row[1])

        if previous_candidate == "":
            previous_candidate = current_candidate # First iteration of loop only
            previous_county = current_county
            poll_result = {current_county : {current_candidate : [0]}} # New test
            # print(poll_result)
                      
        if previous_candidate != current_candidate and previous_county == current_county:
         # New test
            poll_result[current_county][current_candidate] = 0
            previous_candidate = str(row[2])
            new_votes = 0

        if previous_candidate != current_candidate and previous_county != current_county:
            candidate.append(previous_candidate)
            poll_result.__setitem__(current_county, {current_candidate :0})
            poll_result[current_county][current_candidate] = 0
            previous_candidate = str(row[2])
            new_votes = 0


        if previous_candidate == current_candidate:
            poll_result[current_county][current_candidate] = new_votes # tally votes for each candidate
            new_votes += 1

        previous_candidate = current_candidate
        previous_county = current_county

    else:
        candidate.append(current_candidate)

print(poll_result)
candidate_dict = {}
candidate_list = []
for k, v in poll_result.items():
    # print(k,v)
    for x, y in v.items():
        # print(x,y)
        if x not in candidate_list:
            candidate_list.append(x)
            candidate_dict[x]=0
        candidate_dict[x]+=y

print(candidate_dict)
total = sum(candidate_dict.values())
result = {key: (value / total) * 100 for key, value in candidate_dict.items()}
print(result)

# counties = list(poll_result.keys())
# print(counties)
# print(poll_result[counties[0]]['Diana DeGette'])
# old_votes =[]
# for a in counties:
#     candidate = list(poll_result[a].keys())
#     votes = list(poll_result[a].values())
#     print(votes)
# print(candidate)



# # for a, b in poll_result:
# #     candidate = poll_result(counties[a][b])
# #     print(candidate)

# # print(poll_result) https://datagy.io/python-nested-dictionary/
# def add_tally(dict_to_iterate):
#     for key, value in dict_to_iterate.items():
#         if type(value) == dict:
#             print(key)
#             add_tally(value)
#         else:
             
#             print(key, value)

# add_tally(poll_result)
# print(poll_result['Jefferson'])
# print(poll_result['Denver'])
# print(poll_result['Arapahoe'])
# # Tally votes for each candidate from each county
# # print(poll_result[0])
# # for votes in range (0, 9, 3):
# #     vote_total1 += candidate_total_votes[votes]
    
# # for votes in range (1, 9, 3):
# #     vote_total2 += candidate_total_votes[votes]

# # for votes in range (2, 9, 3):
# #     vote_total3 += candidate_total_votes[votes]

# Determine winner of election and assign to a variable called winner

# winner = ""
# if vote_total1 > vote_total2 and vote_total1 > vote_total3:
#     winner = candidate[0]
# if vote_total2 > vote_total1 and vote_total2 > vote_total3:
#     winner = candidate[1]
# if vote_total3 > vote_total1 and vote_total3 > vote_total2:
#     winner = candidate[2]

# Create output for polling data and print

# output = f"""
# Election Results
#   -------------------------
#   Total Votes: {"{:,}".format(total_count)}
#   -------------------------
#   {candidate[0]}: {round((vote_total1 / total_count),5) * 100}% ({"{:,}".format(vote_total1)})
#   {candidate[1]}: {round((vote_total2 / total_count),5) * 100}% ({"{:,}".format(vote_total2)})
#   {candidate[2]}: {"{:.3f}".format((vote_total3 / total_count) * 100)}% ({"{:,}".format(vote_total3)})
#   -------------------------
#   Winner: {winner}
#   -------------------------
# """
# print(output)

# write the output to a new text file called poll_result.
