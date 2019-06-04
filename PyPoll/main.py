#Import the necessary modules
import csv

file_name = "/Users/camila.bonfante/python-challenge/PyPoll/election_data.csv"

# SEEMS LIKE I OVER DID IT?
Voter_ID_count = []
Unique_Candidate = set()
Candidate_0 = []
count_voters = 0
count_voters0 = 0
count_voters1 = 0
count_voters2 = 0
count_voters3 = 0

# Open and read the CSV file, created a Dictionary so the row names are easy to reference
with open(file_name) as csv_file:

    fieldnames = ['Voter ID', 'County', 'Candidate']
    csv_reader = csv.DictReader(csv_file, delimiter=',', fieldnames=fieldnames)

# Took header out
    header = next(csv_file)

    for row in csv_reader:
# The total number of votes cast
        count_voters = count_voters + 1
        Voter_ID_count.append(count_voters)
        final_count = count_voters

# A complete list of candidates who received votes - SEEMS LIKE THERE IS AN EASIER WAY TO DO THIS? Count.

        Unique_Candidate.add(row['Candidate'])
        Unique_Candidate_list = list(Unique_Candidate)

# The total number of votes each candidate won

        if row['Candidate'] == Unique_Candidate_list[0]:
            count_voters0 = count_voters0 + 1
            Candidate_0.append(count_voters0)

        elif row['Candidate'] == Unique_Candidate_list[1]:
            count_voters1 = count_voters1 + 1
            Candidate_0.append(count_voters1)

        elif row['Candidate'] == Unique_Candidate_list[2]:
            count_voters2 = count_voters2 + 1
            # Candidate_2.append(count_voters2)
            Candidate_0.append(count_voters2)
        elif row['Candidate'] == Unique_Candidate_list[3]:
            count_voters3 = count_voters3 + 1
            # Candidate_3.append(count_voters3)
            Candidate_0.append(count_voters3)
        else:
            print(" ")

# WHY CAN'T I GET THE NAME - SEEMS LIKE THERE IS AN EASIER WAY TO DO THIS?
Winner = max(count_voters0,count_voters1,count_voters2,count_voters3)
Winner_Index = Candidate_0.index(Winner)
Winner_Name = Candidate_0[Winner_Index]

# print(Winner, Winner_Index, Winner_Name)


# WHY IS IT ROUNDING DIFFERENTLY EVERY TIME IT RUNS?
perc_0 = round((count_voters0/final_count*100),3)
perc_1 = round((count_voters1/final_count*100),3)
perc_2 = round((count_voters2/final_count*100),3)
perc_3 = round((count_voters3/final_count*100),3)

# WHY ARE THE NAMES CHANGING POSITION IF THE FILE SORTING NEVER CHANGES?
print("Election Results")
print("--------------------------------------")
print(f'Total Votes: {final_count}')
print("--------------------------------------")
print(f'{Unique_Candidate_list[0]}: {perc_0}% ({count_voters0})')
print(f'{Unique_Candidate_list[1]}: {perc_1}% ({count_voters1})')
print(f'{Unique_Candidate_list[2]}: {perc_2}%  ({count_voters2})')
print(f'{Unique_Candidate_list[3]}: {perc_3}% ({count_voters3})')
print("--------------------------------------")
print(f'Winner: {Winner_Name}')
print("--------------------------------------")


# WHY THE LINES ARE NOT SPLITTED OUT/FORMATTED LIKE I OUTLINED BELOW
output = open('pypoll.txt','w')

output.write("Election Results")
output.write("--------------------------------------")
output.write(f'Total Votes: {final_count}')
output.write("--------------------------------------")
output.write(f'{Unique_Candidate_list[0]}: {perc_0}% ({count_voters0})')
output.write(f'{Unique_Candidate_list[1]}: {perc_1}% ({count_voters1})')
output.write(f'{Unique_Candidate_list[2]}: {perc_2}%  ({count_voters2})')
output.write(f'{Unique_Candidate_list[3]}: {perc_3}% ({count_voters3})')
output.write("--------------------------------------")
output.write(f'Winner: {Winner_Name}')
output.write("--------------------------------------")

output.close()
