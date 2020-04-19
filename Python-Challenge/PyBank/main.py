import os
import csv

budget_data_csv = os.path.join('Resources', 'budget_data.csv')

with open(budget_data_csv, 'r') as f:
    
    csv_reader = csv.reader(f)
    next(csv_reader)
    month = 0
    total_months = 0
    profit_loss = 0
    av_change = 0
    date_col = None
    previous_row = int(next(csv_reader)[1])
    net_change_list = []
    greatest_sd_decrease = ["", 0.0]
    greatest_sd_increase = ["",  99]
    
    for row in csv_reader:
        net_change = int(row[1]) - previous_row
        previous_row = int(row[1])
        net_change_list = net_change_list + [net_change]
        net_change_month = row[0]
        total_months += 1
        
        profit_loss += int(row[1])
        if net_change <greatest_sd_decrease[1]:
            greatest_sd_decrease[1] = net_change
            greatest_sd_decrease[0] = net_change_month
        elif net_change > greatest_sd_increase[1]:
            greatest_sd_increase[1] = net_change
            greatest_sd_increase[0] = net_change_month

net_average = sum(net_change_list) / len(net_change_list)

print("Financial Analysis")
print("---------------------------")
print(f" Total Months:{total_months}")
print(f" Total: ${profit_loss}")
print(f"Average Change: ${net_average}")
print(f"Greatest Increase in Profits: {greatest_sd_increase[0]}, ${greatest_sd_increase[1]}")
print(f"Greatest Decrease in Profits: {greatest_sd_decrease[0]}, ${greatest_sd_decrease[1]}") 

