import os
import csv

#create csv path
budget_data_csv = os.path.join( "Resources", "budget_data.csv")

#open and read csv, total months
with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

 #skip the header row
    csv_header = next(csvfile)

#set variables
    month_count = []
    total_profit = []
    profit_change = []
    
                      
    #iterate through the values and add them to the empty list 
    for row in csvreader:
        month_count.append(row[0])
        total_profit.append(int(row[1]))
    for i in range(len(total_profit)-1):
        profit_change.append(total_profit[i+1]-total_profit[i])
                      
#find max and min
increase = max(profit_change)
decrease = min(profit_change)
month_increase = profit_change.index(max(profit_change))+1
month_decrease = profit_change.index(min(profit_change))+1


#print out analysis
print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(month_count)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")      

output = os.path.join(".", 'output.txt')
with open(output,"w") as new:
    new.write("Financial Analysis")
    new.write("\n")
    new.write("------------------------")
    new.write("\n")
    new.write(f"Total Months:{len(month_count)}")
    new.write("\n")
    new.write(f"Total: ${sum(total_profit)}")
    new.write("\n")
    new.write(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")
    new.write("\n")
    new.write(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
    new.write("\n")
    new.write(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")