import os
import csv


# open file path
election_data_csv = os.path.join( "Resources", "electiondata.csv")

#open and read csv
with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


    #skip the header row
    csv_header = next(csvfile)

    #Create dictionary for poll.
    poll = {}

    #Set variable.
    total_votes = 0

    # vote count
    for row in csvreader:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
 
#create list for canidates and number of votes
candidates = []
number_votes = []

#put info into lists
for id, value in poll.items():
    candidates.append(id)
    number_votes.append(value)

# creates vote percent list
vote_percent = []
for i in number_votes:
    vote_percent.append(round(i/total_votes*100, 3))

# zip candidates, number of votes, and vote percent
zip_data = list(zip(candidates, number_votes, vote_percent))

#create winner list to account for ties
winner_list = []

for name in zip_data:
    if max(number_votes) == name[1]:
        winner_list.append(name[0])

# winner list
winner = winner_list[0]

for w in range(1, len(winner_list)):
        winner = winner + ", " + winner_list[w]

#print to text file
election_results = os.path.join("election_results.txt")

with open(election_results, 'w') as txtfile:
    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for entry in zip_data:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

#print to git bash
with open(election_results, 'r') as readfile:
    print(readfile.read())