# File Display
# 07/04/2017
# CTI-110 M5T1 - File Display
# Eric Hadley


    
import random

# Open the file.
myfile = open('ehnumbers.txt', 'w')

#Write random numbers to the file.
for count in range(5):
    number = random.randint(1, 500)
    myfile.write(str(number) + '\n')

# Close the file
myfile.close()



