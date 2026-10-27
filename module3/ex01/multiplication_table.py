#!/usr/bin/env python3

try:
	number = int(input("Enter a number: "))
	i = 0
	while i < 10:
		multiply = i * number
		print(i, "x", number, "=", multiply)
		i += 1
except ValueError:
	print("ERROR: The value passed is wrong!!")