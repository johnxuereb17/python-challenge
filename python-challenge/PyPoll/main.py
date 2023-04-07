import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join("Resources/election_data.csv")

# Create empty dictionaries to store the candidate and vote count data
candidate_votes = {}
unique_candidates = []

# Initialize variables
total_votes = 0
winner = ""
winning_votes = 0

# Open the CSV file and read the data
with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    

    # Skip the header row and loop through each row of data after the header
    header = next(csvreader)
    for row in csvreader:

        # Count the total number of votes
        total_votes += 1

        # Extract the candidate name from the row
        candidate_name = row[2]

        # Add the candidate to the unique candidates list if they are not already in it
        if candidate_name not in unique_candidates:
            unique_candidates.append(candidate_name)

        # If the candidate is already in the candidate_votes dictionary, add 1 to their vote count
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        # Otherwise, add the candidate to the dictionary with a vote count of 1
        else:
            candidate_votes[candidate_name] = 1

# Print the election results to the terminal and export to a text file
output_path = os.path.join("election_results.txt")
with open(output_path, "w") as txtfile:

    # Print the header and total vote count to the terminal and text file
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")

    
