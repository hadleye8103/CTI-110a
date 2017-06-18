# Bug Collector
# 6/17/2017
# CTI-110 M4T1 - Bug Collector
# Eric Hadley

# Intialize Accumulator
total = 0

# Get bugs collected for each day
for day in range(1, 8):
# Prompt the user
    print('Enter the bugs collected on day', day)

# Input the number of bugs
bugs = int(input ())
# Add bugs to total
total += bugs
# Display the total bugs
print('You collected a total of', total, 'bugs.')
