speed = input("Enter vehicle speed in mph: ")
print(speed)
time = input("Enter number of hours vehicle traveled: ")
print(time)

print("Hour --- Distance Traveled in Miles")

for hour in range(1, time + 1):
    distance = speed * hour
    print(str(hour) + "               " + str(distance)+str(" Miles"))
