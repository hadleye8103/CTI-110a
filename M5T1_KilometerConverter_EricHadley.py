# Kilometer Converter
# 6/29/2017
# CTI-110 M5T1_Kilometer Converter
# Eric Hadley


CONVERSION_FACTOR = 0.6214

def main():
# Get the distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))

# Display the distance converted to miles.
    show_miles(kilometers)

def show_miles(km):
# calculate miles.
    miles = km * CONVERSION_FACTOR

# Display the miles.
    print(km, 'kilometers equals', miles, 'miles.')

main ()
