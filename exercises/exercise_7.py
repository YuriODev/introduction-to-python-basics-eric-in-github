
# counter= 0
# list = []

# for i in num:
# 	list.append(i)

# print(list)

# for i in list:
# 	counter = i + counter

# print(counter)

num = input("Enter a 4-digit integer: ")
counter = 0
for i in num:
    counter += int(i)

print("The sum of the digits is:", counter)