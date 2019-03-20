import os
import csv

csvpath = os.path.join(".","Resources","election_data.csv")
output_path = os.path.join(".", "output", "election_data.txt")

total_votes = 0
candidates = []
candidate_votes = {}
winner_count = 0
winner = ""

with open(csvpath, newline='') as csvfile:

    
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    	
	
    for row in csvreader:
		
        total_votes += 1

        candidate = row[2]
        
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
        
        candidate_votes[candidate] = candidate_votes[candidate] + 1

with open(output_path, 'w') as txt_file:
	
    print()
    print("Election Results\n")
    print("-------------------------")
    print("Total Votes " + str(total_votes))
    print("-------------------------\n")
	
	
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Total Votes " + str(total_votes)+"\n")
    txt_file.write("-------------------------\n")

    
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes)/float(total_votes)*100
        if (votes > winner_count):
            winner_count = votes
            winner = candidate
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)
        txt_file.write(voter_output)
        
    winning_summary = (f"Winner: {winner}")
    print(winning_summary)
    txt_file.write(winning_summary)