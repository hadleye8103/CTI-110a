# Age Classifier
# 6/17/2017
# CTI-110 M3HW1 - Age Classifier
# Eric Hadley

# If the person is 1 year old or less, he or she is an infant.
# If the person is older that 1 year, but younger than 13 years, he or she is a child.
# If the person is at least 13 years old, but less then 20 years old, he or she is a teenager.
# If the person is at least 20 years old, he or she is an adult.

age = int(input('Please enter persons age: '))
if age <=1 print('The person is an infant.')
else:
    print('The person is not an infant.')
    if age > 1 and age > 13: print('The person is a child.')
    else:
        print('The person is not an infant.')
        if age <= 13 and age > 20: print('The person is a teenager.')
        else:
            print('The person is not a teenager.')
            if age >= 20: print('The person is an adult.')
