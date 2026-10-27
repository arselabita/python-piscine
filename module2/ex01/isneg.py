#!/usr/bin/env python3

try :
	number = int(input("Enter a number: "))
	if number < 0:
		print("The number is negative")
	elif number > 0:
		print("The number is positive")
	else:
		print("The number is both positive and negative")
except ValueError:
	print("ERROR: The value passed is not a number")