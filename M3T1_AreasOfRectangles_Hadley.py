# Area of Rectangles
# 6/17/2017
# CTI-110 M3T1 - Area of Rectangles
# Eric Hadley

# Get the dimensions of rectangle 1
length1 = int(input('Enter the length of rectangle1: '))
width1 = int(input('Enter the width of rectangle1: '))

# Get the dimensions of rectangle 2
length2 = int(input('Enter the length of rectangle2: '))
width2 = int(input('Enter the width of regtangle2: '))

# Calculate the areas of the rectangles.
area1 = lenght1 * width1
area2 = length2 * width2

# Determine which has the greater area.
if area1 > area2:
    print('Rectangle 1 has the greater area.')
else:
    if area 2 > area1:
        print('Rectangle 2 has the greater area.')
    else:
        print('Both have the same area.')
