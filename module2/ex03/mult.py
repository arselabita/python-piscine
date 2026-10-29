#!/usr/bin/env python3

try :
	num1 = int(input("Enter the first number: "))
	num2 = int(input("Enter the second number: "))

	multiply = num1 * num2
	print(f"{num1} x {num2} = {multiply}")

	if multiply < 0:
		print("The result is negative.")
	elif multiply > 0:
		print("The number is positive.")
	else:
		print("The number is both positive and negative.")
except ValueError:
	print("ERROR: The value passed is not a number.")