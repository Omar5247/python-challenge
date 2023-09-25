import os
import csv

tot_votes = 0
candidates = {}
winner = ""
win_votes = 0

election_data_csv = os.path.join("Resources", "election_data.csv")

with open(election_data_csv,) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        candidate = row[2]

        tot_votes += 1

        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

for candidate, votes in candidates.items():
    percent = (votes / tot_votes) * 100
    if votes > win_votes:
        win_votes = votes
        winner = candidate


print("Election Results")
print("----------------------------")
print(f"Total Votes: {tot_votes}")
print("----------------------------")
for candidate, votes in candidates.items():
    percentage = (votes / tot_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")


output_file_path = "election_results.txt"
with open(output_file_path, "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Votes: {tot_votes}\n")
    output_file.write("----------------------------\n")
    for candidate, votes in candidates.items():
        percentage = (votes / tot_votes) * 100
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("----------------------------\n")
