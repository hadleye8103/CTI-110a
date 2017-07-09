# Body Mass Index
# 6/17/2017
# CTI-110 M3HW1 - Body Mass Index
# Eric Hadley


weight = float(input('Please enter persons weight in lbs: '))
height = float(input('Please enter persons height in inches: '))
BMI = weight * 703/height * height
if BMI >=18.5 and BMI <=25:
    print('Persons weight is optimal.')
if BMI < 18.5:
    print('Person is underweight.')
if BMI > 25:
    print('Person is overweight.')

