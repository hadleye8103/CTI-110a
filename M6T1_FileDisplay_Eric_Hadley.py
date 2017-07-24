# File Display
# 07/04/2017
# CTI-110 M5T1 - File Display
# Eric Hadley

# Open the file
myfile = open('numbers.txt', 'r')

# Read and display the file's contents.
for line in myfile:
    number = int(line)
    print(number)

# Close the file.
myfile.close()
