# Tip, Tax, Total
# June 10, 2017
# CTI-110 M2 HW2
# Eric Hadley

# Amount of the meal
amount = float(input('How much was the meal? '))

# Amount of tip
tip = amount * .18

# Amount of tax
tax = int(amount) * .07

#The total amount of the meal
print('The tip is', tip)
print('The tax is', tax)
print('The total of the meal is', amount + tip + tax)
