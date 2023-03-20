import os
import csv

#create csv path
csvpath = os.path.join('..', 'Resources', "budget_data.csv")

# set variables
total_month = 0
net_profit_loss = []
first_number = 0
last_number = 0


#open and read csv
with open(budget_data.csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #skip the header row
    csv_header = next(csv_file)

    budget_data = [row for row in budget_data.csv]

print("Total months:" + str(len(budget_data)))