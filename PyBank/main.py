
import csv

file_name = "/Users/camila.bonfante/Desktop/Bootcamp/w3_w4_Python/Homework/03-Python_Homework_PyBank_Resources_budget_data.csv"

with open(file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    csv_converted = [[row[0], int(row[1])] for row in csv_reader]


# loop to count dates
    i = 0

    for row in csv_converted:

        Date = row[0]
        i = i + 1
        final_count = i

# loop to sum profit

    sum_profit = 0

    for row in csv_converted:
        Profit = row[1]

        sum_profit = Profit + sum_profit
        final_profit = sum_profit

# loop to calc average of wins/losses

diff_profit = 0

    for row in csv_converted:
        Profit = row[1]

        diff_profit = Profit - sum_profit


Average = sum_profit/final_count



print()
print("Financial Analysis")
print("---------------------------------------------------------------------")
print("Total Months:"+ " "+ str(i))
print("Total:" + " $"+ str(final_profit))
print("Average  Change:" + " " + str(Average))
# print("Greatest Increase in Profits:" +  " " +)
# print("Greatest Decrease in Profits:" + " " +)



