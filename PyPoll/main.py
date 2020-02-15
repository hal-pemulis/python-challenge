#PyPoll

# Import modules
import os
import csv

# Create empty lists
vote_list = []
candidates = []
votes = []

csvpath = os.path.join('..', 'CSV_files', 'election_data.csv')

# Open csv file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Skip header
    csv_header = next(csvreader)

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

# Create new path and txt file to write results to
txtpath = os.path.join('..', 'CSV_files', 'results.txt')

with open(txtpath, 'a') as txtfile:

    txtfile.write('Election Results\r-------------------------\r')
    txtfile.write(f'Total votes: {total_votes}')
    txtfile.write('\r-------------------------\r')
    for x in candidates:
        txtfile.write(f'{x}: {round((votes[candidates.index(x)]/total_votes*100), 2)}% ({votes[candidates.index(x)]} votes)\r')
    txtfile.write('-------------------------\r')
    txtfile.write(f'Winner: {candidates[votes.index(max(votes))]}')

    txtfile.close()
