#PyPoll

import os
import csv

vote_list = []
candidates = []
votes = []

with open('election_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    next(csvreader, None)

    for row in csvreader:
        vote_list.append(row[2])
        if row[2] not in candidates:
            candidates.append(row[2])

    total_votes = int(len(vote_list))

    for candidate in candidates:
        total = 0
        for i in vote_list:
            if candidate in i:
                total += 1
        votes.append(total)

    print('Election Results\r-------------------------')
    print(f'Total votes: {total_votes}')
    print('-------------------------')
    for x in candidates:
        print(f'{x}: {(votes[candidates.index(x)]/total_votes)*100}% ({votes[candidates.index(x)]} votes)')
    print('-------------------------')
    print(f'Winner: {candidates[votes.index(max(votes))]}')

    csvfile.close()
