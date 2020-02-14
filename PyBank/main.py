#PyBank

import os
import csv

with open('budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    next(csvreader, None)

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
        #print(row)

    # print(months)
    # print(profit_loss[0]+profit_loss[0])

    for i in profit_loss)-1):
        print(profit_loss[i+1] - profit_loss[i])


    print(f'Total Months: {total_months}')
    print(f'Total: {net_total}')
    print(f'Average Change: {sum(profit_loss)/len(profit_loss)}')
    print(f'Greatest Increase in Profits: {months[profit_loss.index(max(profit_loss))]} ({max(profit_loss)})')
    print(f'Greatest Decrease in Profits: {months[profit_loss.index(min(profit_loss))]} ({min(profit_loss)})')

csvfile.close()
 

