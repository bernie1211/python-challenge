import csv

# We want to read the election data from the csv file
with open('election_data.csv', 'r') as f:
    csv_reader = csv.reader(f, delimiter= ',')
    next(csv_reader) # To skip the header row

# These are lists and values
    number_votes = {}
    candidates = []
    voters = []
        
    for row in csv_reader:
        voters.append(row[0])
        if row[2] not in number_votes:
            number_votes[row[2]] = 0
            candidates.append(row[2])
            number_votes[row[2]] += 1 

# We want the total number of votes in the set
total_votes = len(voters)

# We want the vote percent for candidates
vote_percents = []
for value in number_votes.values():
    vote_percents.append(value/total_votes*100)
vote_percents = [round(percent, 2) for percent in vote_percents] 

# We want the total votes
vote_totals = []
for value in vote_tallies.values():
    vote_totals.append(value)

# We want the election results
election_result = []
for _ in range(len(candidates)):
    election_results.append(f"{candidates[_]}: {vote_percents[_]} ({number_votes[_]})")

# We want to find the candidate with the most votes
most_votes = max(number_votes.values())
top_candidate = [i for i, v in number_votes.items() if v == most_votes]

# We want an analysis report
print(f"Election Results")
print("-------------------")
print(f"Total Votes: {total_votes}")
print("--------------------")
print(f"Top Candidate: {top_candidate}")
print("---------------------")

