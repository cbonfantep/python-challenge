
#Import the necessary modules
import csv

file_name = "/Users/camila.bonfante/Desktop/Bootcamp/w3_w4_Python/Homework/03-Python_Homework_PyBank_Resources_budget_data.csv"

total_months = 0
sum_profit = 0
change = 0
Diff_Profits = []
Dates = []

# Open and read the CSV file
with open(file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
# Reading the header row
    header = next(csv_reader)
# New file without header, convert Profit to integer
    # csv_reader = [[row[0], int(row[1])] for row in csv_reader]

    first_row = next(csv_reader)
    diff_profit = int(first_row[1])
    sum_profit = int(first_row[1])

# loop to count dates
    for row in csv_reader:

        Date = row[0]
        total_months = total_months + 1
        final_month_count = total_months + 1
        Dates.append(row[0])

# loop to sum profit

        Profit = int(row[1])
        sum_profit = Profit + sum_profit
        final_profit = sum_profit

# loop to calc average of wins/losses and create a list called Diff_Profits to store the numbers

        change = int(row[1])-diff_profit
        Diff_Profits.append(change)
        diff_profit = int(row[1])

#Greatest increase in profits, decrease and average change - outside of the loop

final_change = sum(Diff_Profits)/(total_months)

greatest_increase = max(Diff_Profits)
increase_index = Diff_Profits.index(greatest_increase)
increase_date = Dates[increase_index]

greatest_decrease = min(Diff_Profits)
decrease_index = Diff_Profits.index(greatest_decrease)
decrease_date = Dates[decrease_index]


print("Financial Analysis")
print("---------------------------------------------------------------------")
print("Total Months:"+ " "+ str(final_month_count))
print("Total:" + " $"+ str(final_profit))
print("Average Change:" + " $" + str(round(final_change,2)))
print("Greatest Increase in Profits: " +str(increase_date) +  " ($" +str(greatest_increase)+")")
print("Greatest Decrease in Profits: " +str(decrease_date) + " ($" +str(greatest_decrease)+")")

output = open('pybank.txt','w')

output.write("\nFinancial Analysis")
output.write("\n---------------------------------------------------------------------")
output.write("\nTotal Months:"+ " "+ str(final_month_count))
output.write("\nTotal:" + " $"+ str(final_profit))
output.write("\nAverage Change:" + " $" + str(round(final_change,2)))
output.write("\nGreatest Increase in Profits: " +str(increase_date) +  " ($" +str(greatest_increase)+")")
output.write("\nGreatest Decrease in Profits: " +str(decrease_date) + " ($" +str(greatest_decrease)+")")

output.close()

