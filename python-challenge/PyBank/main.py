import csv

# Defining Variables
total_months = 0
total_profit_loss = 0
profit_loss_changes = []
greatest_increase = ['', 0]
greatest_decrease = ['', 999999999999999999]

# open and read file while skipping header
with open('Resources/budget_data.csv') as budget_data:
    reader = csv.reader(budget_data)

    header = next(reader)
    
    # Loop through each row 
    for row in reader:
        
        # Keep adding on to the total number of months
        total_months += 1
        
        # Add the profit/loss to the total
        total_profit_loss += int(row[1])
        
        # Calculate the change in profit/loss
        if total_months > 1:
            profit_loss_changes.append(int(row[1]) - previous_profit_loss)
            
            # Check for the greatest increase/decrease in profits
            if (int(row[1]) - previous_profit_loss) > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = int(row[1]) - previous_profit_loss
            
            if (int(row[1]) - previous_profit_loss) < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = int(row[1]) - previous_profit_loss
        
        # Store the current profit/loss for the next iteration
        previous_profit_loss = int(row[1])

# Calculate the average change in profit/loss
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Print entire financial analysis 
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Export financial analysis to a text file
with open('financial_analysis.txt', 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profit_loss}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")