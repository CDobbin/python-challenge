# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast


# Define lists and dictionaries to track candidate names and vote counts
candidates_votes = {}

# Winning Candidate and Winning Count Tracker
winner = ""
winning_count = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(".\/,", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates_votes:
            candidates_votes[candidate_name] = 0

        # Add a vote to the candidate's count
        candidates_votes[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    election_results = ( " \n" 
        f"Election Results\n"
        f"----------------\n"
        f"Total Votes: {total_votes}\n"
        f"----------------\n")
    print(election_results)

    # Write the total vote count to the text file
    txt_file.write(election_results)

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate, votes in candidates_votes.items():

        # Get the vote count and calculate the percentage
        vote_percentage = (votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes
            winner = candidate

        # Print and save each candidate's vote count and percentage
        candidate_results = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(candidate_results)
        txt_file.write(candidate_results)

    # Generate and print the winning candidate summary
    winner_summary = (f"----------------\n"
        f"Winner: {winner}\n"
        f"----------------\n")
    print(winner_summary)
    
    # Save the winning candidate summary to the text file
    txt_file.write(winner_summary)