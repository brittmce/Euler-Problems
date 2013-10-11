## This program calculates the sum of all numbers below 1000 that are factors of 3 and/or 5.

number = 1
count = 0
set = []
sum = 0

while number < 1000:
	if number % 3 == 0 or number % 5 == 0:
		count += 1
		set.append (number)
		sum += number
		number += 1
	else:
		number += 1
		
print sum