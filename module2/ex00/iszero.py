#!/usr/bin/env python3

try:
	number = int(input("Enter a number: "))
	if number == 0 :
		print("This number is equal to zero")
	else :
		print("This number is different from zero")
except ValueError:
	print("ERROR: The value you are passing is not a number!")