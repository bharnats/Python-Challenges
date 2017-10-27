import csv
import os
import collections

# file path
filePath = "pyPoll.csv"

# declare an empty list to hold the voters ID, and list of candidates
votersList = []
candidate = []

# open the csv file to read the poll data
with open(filePath, newline="") as csvFile:
    fileReader = csv.DictReader(csvFile, delimiter=",")
    for row in fileReader :
        # Add Items to voters List
        votersList.append(row["Voter ID"])
        # Add items to candidate List
        candidate.append(row["Candidate"])
        
        
    
    # create a list of unique candidates
    candidateList = set(candidate)

    from collections import Counter
    # counter function returns a dictionary with number of occurances for each key
    vote_counter = Counter(candidate)

    candidate_list = list(vote_counter.keys())
    total_votes_list = list(vote_counter.values())

    # find percentages of votes for each candidate
    percent_votes_list = [round((i/len(votersList)) * 100) for i in total_votes_list]

    # printing out the results to the terminal
    print("                 ")
    print("Election Results")
    print("---------------------------")
    print(f'Total Votes: {len(votersList)}')
    print("----------------------------")

    # print the results for each candidate
    for j in range(len(candidate_list)) :
        print(f'{candidate_list[j]}: {percent_votes_list[j]}% ({total_votes_list[j]})')
    print("--------------------------------")
    print(f'Winner: {max(vote_counter, key=vote_counter.get)}')
    print("---------------------------------")

    # open a text file to write the results into..
    output_filepath = "OutPyPoll.txt"
    with open(output_filepath,"w") as write_file :
        
        # write the results to a text file
        write_file.write('\nElection Results\n')
        write_file.write("-----------------------------------\n")
        write_file.write('Total Votes: %s\n' %len(votersList))
        write_file.write('-----------------------------------\n')
        for j in range(len(candidate_list)) :
            write_file.write('%s' %candidate_list[j]) 
            write_file.write(': %s' %percent_votes_list[j])
            write_file.write('% ')
            write_file.write('(')
            write_file.write('%s' %total_votes_list[j])
            write_file.write(')\n')
        write_file.write('--------------------------------\n')
        write_file.write('Winner: %s' %max(vote_counter, key=vote_counter.get))