#!/usr/bin/env python3

user_input = input("Give me a number: ").strip()
try:
	num = float(user_input)
	if num.is_integer():
		print(f"This number is an integer.")
	else:
		print(f"This number is a decimal.")
except ValueError:
	print("ERROR: Pass a number!")