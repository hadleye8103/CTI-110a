# Sum of Numbers
# 6/23/2017
#CTI-110 M4HW1 - Sum of Numbers
# Eric Hadley


total = 0
number = 0

# Explain what we are doing.
print('This program calculates the sum of')
print('numbers you will enter.')
print('enter negative number to end.')

# Get the numbers and accumulate them.
while number  >= 0 :
        number = int(input('Enter a number: '))
        total = total + number


# Display the total of the numbers.
print('The total is', total)
