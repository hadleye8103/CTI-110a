# Sales Prediction
# 6-9-2017
# CTI-110 M2T1 Sales Prediction
# Eric Hadley

# Get the total projected sales
total_sales = float(input('Enter the projected sales: '))

# Calculate the profit as 23 percent of total sales
profit = total_sales * 0.23

# Display the profit
print('The profit is $', format(profit, ',.2f'))
