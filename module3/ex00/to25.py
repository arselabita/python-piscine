#!/usr/bin/env python3

try:
	number = int(input("Enter a number less than 25: "))
	if number < 25:
		i = number
		while i <= 25:
			print("Inside the loop, my variable is ", i)
			i+=1
	else:
		print("Error")
except ValueError:
	print("ERROR: The value passed is wrong!!")