import csv

# We want to read the budget data from the csv file
with open('./Resources/budget_data.csv', 'r') as f:
    csv_reader = csv.reader(f, delimiter= ',')
    next(csv_reader) # To skip the header row

    months = []
    profit_losses = []
    changes = []
        
    for row in csv_reader:
        months.append(row[0])
        profit_losses.append(int(row[1]))

# We want to add the total of months
to_months = len(months)

# We want to add the total of profit/losses
net_total = sum(profit_losses)

# We want to get the sum in profit/losses into a list
for i in range(1, to_months):
    change = profit_losses[i] - profit_losses[i-1]
    changes.append(change)

# We want to find the average of change
average_change = sum(changes) / len(changes)

# We want the greatest increase and decrease in profits
greatest_increase_pro = max(changes)
greatest_increase_date = months[changes.index(greatest_increase_pro) + 1]
greatest_decrease_loss = min(changes)
greatest_decrease_date = months[changes.index(greatest_decrease_loss) + 1]

output = "financial analysis\n"
output += "--------------------------\n"
output += f"toatl months: {to_months}\n"
output += f"total: ${net_total}\n"
output += f"average change: ${average_change: .2f}\n"
output += f"greatest increase in profits: {greatest_increase_date} (${greatest_increase_pro})\n"
output += f"greatest decrease in profits: {greatest_decrease_date} (${greatest_decrease_loss})\n"

print(output)
# # We want to make an analysis report
# print("financial analysis")
# print("--------------------------")
# print(f"toatl months: {to_months}")
# print(f"total: ${net_total}")
# print(f"average change: ${average_change: .2f}")
# print(f"greatest increase in profits: {greatest_increase_date} (${greatest_increase_pro})")
# print(f"greatest decrease in profits: {greatest_decrease_date} (${greatest_decrease_loss})")


with open('./Analysis/Analysis.txt', 'w') as f:
    f.write(output)