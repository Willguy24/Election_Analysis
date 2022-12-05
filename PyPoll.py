# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initalize a total vote counter
total_votes = 0

#candidate options and candidate votes
candidate_options = []
candidate_votes ={}

#Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Read and print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count.
        total_votes += 1

        #Print the candidate name for each row
        candidate_name = row[2]

        #if candidate doesnt match existing candidate
        if candidate_name not in candidate_options:
            #add to list of candidate
            candidate_options.append(candidate_name)

            #Begin tracking that candidate votes
            candidate_votes[candidate_name] = 0
        #Give a vote to the canidate
        candidate_votes[candidate_name] += 1

    #Save the results to our text file
    with open(file_to_save, "w") as txt_file:
        #Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        #Save the final vote count to the text file.
        txt_file.write(election_results)
        

        #Iterate through the canidate list
for candidate_name in candidate_votes:
    #Retrieve vote count of a canidate
    votes = candidate_votes[candidate_name]
    #Calculate percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    #Print the canidate name and percentage of votes.
    print(f"{candidate_name}: revieved {vote_percentage:.1f}% of the vote.")

    #Print out each canidates name, vote count and percentage of votes to terminal
    #print(f"{candidate_name}:{vote_percentage:.1F}%({votes:,})\n")

    #Determine winning vote count and candidate
    #Determine if the votes is greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #if true then set winning_count = votes and winning_percent = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        #and set the winning candidate equal to the candidates name
        winning_candidate = candidate_name

    #print out the winning candidate vote count and percentage to terminal
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
#print(winning_candidate_summary)

#Print the candidate list
print(candidate_votes)