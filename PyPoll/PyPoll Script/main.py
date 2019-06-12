import os, csv

tot_votes = 0
candidate = ""
candidate_votes = {}
candidate_percent = {}
winner_votes = 0
winner = ""

filepath = os.path.join("..", "election_data.csv")

with open(filepath,'r', newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader = next(csvreader, None)


    # votes
    for row in csvreader:
        tot_votes = tot_votes + 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] = candidate_votes[candidate] + 1
        else:
            candidate_votes[candidate] = 1



# voter pecent and winner
for person, vote_count in candidate_votes.items():
    candidate_percent[person] = '{0:.0%}'.format(vote_count / tot_votes)
    if vote_count > winner_votes:
        winner_votes = vote_count
        winner = person

dash = ("-" * 20)

# print out results
print("Election Results")
print(dash)
print(f"Total Votes: {tot_votes}")
print(dash)
for person, vote_count in candidate_votes.items():
    print(f"{person}: {candidate_percent[person]} ({vote_count})")
print(dash)
print(f"Winner: {winner}")
print(dash)


# with open("PollOutput.txt", "w") as output:
#     for t in output:
#         output.write(tot_votes)
        # output.write("Winner: " + winner)
        # # for person, vote_count in candidate_votes.items():
        # #     output.write(f"{person}: {candidate_percent[person]} ({vote_count})"
        # output.write(f"{person}: {candidate_percent[person]} ({vote_count})")

