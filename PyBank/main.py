#PyBank

# import modules
import os
import csv

# set variable to file path
csvpath = os.path.join('..', 'CSV_files', 'budget_data.csv')

# access file and begin loop
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Skip/store header
    csv_header = next(csvreader)
    
    # set variables to 0 and empty lists
    total_months = 0
    net_total = 0
    months = []
    profit_loss = []
    average_change = []

    # begin loop through CSV rows
    for row in csvreader:
        
        # for every row, add 1 to 'total months'
        total_months += 1
        
        # add every row's 'profit/loss' to 'net_total' variable
        net_total += int(row[1])
        
        # serperate months and profit/loss into different lists... 
        # by appending as the program loops through the rows...
        # ('zip' may save space here and be more efficient, but I thought this was more intuitive)
        months.append(row[0])
        profit_loss.append(int(row[1]))

    # done with CSV file
    csvfile.close()

# begin loop through 'profit_loss' list to create list of changes
for i in range(len(profit_loss)):
    
    # conditional to skip the first position in list
    if i > 0:
        # calculates every change between months and appends to 'average_change' list
        average_change.append(profit_loss[i] - profit_loss[i-1])

# prints 'total_months' (aka number of rows minus header)
print(f'Total Months: {total_months}')

# prints 'net_total' (sum of profit/loss)
print(f'Total: {net_total}')

# calculates and prints average change by adding all the numbers... 
# in 'average_change' and dividing sum by lenth of the list 
print(f'Average Change: {int(sum(average_change)/len(average_change))}')

# calculates and prints the month and number of the greatest increase in profits...
# by find the max number in 'profit_loss' list and referencing that same position...
# in the 'months' list
print(f'Greatest Increase in Profits: {months[profit_loss.index(max(profit_loss))]} ({max(profit_loss)})')

# same for the lowest number in 'profit_loss' list
print(f'Greatest Decrease in Profits: {months[profit_loss.index(min(profit_loss))]} ({min(profit_loss)})')

# set variable to new file path 
txtpath = os.path.join('..', 'results', 'budget_data.txt')

# create new text file and begin loop
with open(txtpath, 'w') as txtfile:
    
    # write the same information to the new text file...
    # (probably a better and more efficient way to do this)
    txtfile.write(f'Total Months: {total_months}\r')
    txtfile.write(f'Total: {net_total}\r')
    txtfile.write(f'Average Change: {int(sum(average_change)/len(average_change))}\r')
    txtfile.write(f'Greatest Increase in Profits: {months[profit_loss.index(max(profit_loss))]} ({max(profit_loss)})\r')
    txtfile.write(f'Greatest Decrease in Profits: {months[profit_loss.index(min(profit_loss))]} ({min(profit_loss)})\r')

    # close the newly created text file
    txtfile.close()
    