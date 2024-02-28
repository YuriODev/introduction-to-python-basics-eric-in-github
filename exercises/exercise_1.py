numbers = input("Enter 5 numbers: ")
list = []
for number in numbers:
	number = int(number)
	list.append(number)

a = list [0] + list[2] + list[4]


b = list[1] + list[3]

final = str(a) + str(b)

print(final)