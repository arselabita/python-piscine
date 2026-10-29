#!/usr/bin/env python3

try:
	num1 = int(input("Give me the first number: "))
	num2 = int(input("Give me the second number: "))

	print("Thank you!")

	# multiply = num1 * num2
	substract = num1 - num2
	divide = num1 / num2
	add = num1 + num2

	print(f"{num1} * {num2} = { num1 * num2}")
	print(f"{num1} - {num2} = {substract}")
	print(f"{num1} / {num2} = {divide}")
	print(f"{num1} + {num2} = {add}")

except ValueError:
	print("ERROR: Careful pass a number!")
