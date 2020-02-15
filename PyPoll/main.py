#PyPoll

# Import modules
import os
import csv

# Create empty lists
vote_list = []
candidates = []
votes = []

# Open csv file
with open('election_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Skip header
    next(csvreader, None)

    # Begin loop through csv data
    for row in csvreader:
        
        # Add each voter's candidate to vote_list list
        vote_list.append(row[2])
        
        # Add each different candidate to candidates list
        if row[2] not in candidates:
            candidates.append(row[2])
    
    # Close file
    csvfile.close()

# Find total votes by counting number of items in list
total_votes = int(len(vote_list))

# Loop through candidates list
for candidate in candidates:
    
    # Set/Reset each candidate's votes to zero
    total = 0
    
    # Loop through the votes
    for i in vote_list:
        
        # If a vote matches the candidate, add 1 to 'total'
        if candidate in i:
            total += 1
            
    # Add the candidate's total to the 'votes' list
    votes.append(total)

# Begin printing results
print('Election Results\r-------------------------')
print(f'Total votes: {total_votes}')
print('-------------------------')

# Determine and print results by referencing 
# indexes between 'votes' and 'candidates' lists
for x in candidates:
    print(f'{x}: {round((votes[candidates.index(x)]/total_votes*100), 2)}% ({votes[candidates.index(x)]} votes)')
print('-------------------------')

# Prints winner by finding index of max of 'votes' list
print(f'Winner: {candidates[votes.index(max(votes))]}')

# Create new file to write results to
with open('newcsv.csv', 'w', newline='') as newcsv:
    csvwriter = csv.writer(newcsv.csv, delimiter = ',')

    csvwriter.writerow('Election Results\r-------------------------')
    csvwriter.writerow(f'Total votes: {total_votes}')
    csvwriter.writerow('-------------------------')
    for x in candidates:
        csvwriter.writerows(f'{x}: {round((votes[candidates.index(x)]/total_votes*100), 2)}% ({votes[candidates.index(x)]} votes)')
    csvwriter.writerow('-------------------------')
    csvwriter.writerow(f'Winner: {candidates[votes.index(max(votes))]}')

    newcsv.close()
