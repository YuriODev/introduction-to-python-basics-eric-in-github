seconds = int(input("Enter number of seconds since the beginning of day"))
hours = seconds/60
hours = hours/60
minutes = seconds % 60
print(hours, minutes, seconds)