# Age Classifier
# 6/17/2017
# CTI-110 M3HW1 - Age Classifier
# Eric Hadley


mass = int(input('Please enter persons mass: '))
newtons = mass * 9.8
if newtons > 500: print('Object is too heavy.')
else:
    if newtons < 100: print('Object is too light.')
