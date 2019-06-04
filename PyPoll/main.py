#Import the necessary modules
import csv

file_name = "/Users/camila.bonfante/python-challenge/PyPoll/election_data.csv"

Voter_ID_count = []
County = []
Unique_Candidate = set()
count_voters = 0

# Open and read the CSV file
with open(file_name) as csv_file:
    # csv_reader = csv.reader(csv_file, delimiter=',')
# Reading the header row
#     header = next(csv_reader)

    fieldnames = ['Voter ID', 'County', 'Candidate']
    csv_reader = csv.DictReader(csv_file, delimiter=',', fieldnames=fieldnames)

    for row in csv_reader:
#The total number of votes cast
        count_voters = count_voters + 1
        Voter_ID_count.append(count_voters)
        final_count = count_voters

# A complete list of candidates who received votes

        Unique_Candidate.add(row['Candidate'])
print(Unique_Candidate)



print("Election Results")
print("--------------------------------------")
print("Total Votes: "+ str(final_count))
print("--------------------------------------")

# print("Total:" + " $"+ str(final_profit))
# print("Average Change:" + " $" + str(round(final_change,2)))
# print("Greatest Increase in Profits: " +str(increase_date) +  " ($" +str(greatest_increase)+")")
# print("Greatest Decrease in Profits: " +str(decrease_date) + " ($" +str(greatest_decrease)+")")

