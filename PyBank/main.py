#PyBank

import os
import csv

csvpath = os.path.join('..', 'CSV_files', 'budget_data.csv')


with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Skip header
    csv_header = next(csvreader)

    total_months = 0
    net_total = 0
    months = []
    profit_loss = []
    average_change = []

    for row in csvreader:
        total_months += 1
        net_total += int(row[1])
        months.append(row[0])
        profit_loss.append(int(row[1]))

    csvfile.close()

for i in range(len(profit_loss)):
    if i > 0:
        average_change.append(profit_loss[i] - profit_loss[i-1])

print(f'Total Months: {total_months}')
print(f'Total: {net_total}')
print(f'Average Change: {int(sum(average_change)/len(average_change))}')
print(f'Greatest Increase in Profits: {months[profit_loss.index(max(profit_loss))]} ({max(profit_loss)})')
print(f'Greatest Decrease in Profits: {months[profit_loss.index(min(profit_loss))]} ({min(profit_loss)})')


txtpath = os.path.join('..', 'CSV_files', 'budget_data.txt')

with open(txtpath, 'w') as txtfile:

    txtfile.write(f'Total Months: {total_months}\r')
    txtfile.write(f'Total: {net_total}\r')
    txtfile.write(f'Average Change: {int(sum(average_change)/len(average_change))}\r')
    txtfile.write(f'Greatest Increase in Profits: {months[profit_loss.index(max(profit_loss))]} ({max(profit_loss)})\r')
    txtfile.write(f'Greatest Decrease in Profits: {months[profit_loss.index(min(profit_loss))]} ({min(profit_loss)})\r')

    txtfile.close()
