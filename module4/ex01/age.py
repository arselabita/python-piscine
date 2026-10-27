#!/usr/bin/env python3

try:
	input = int(input("Please tell me your age: "))

	print("You are currently", input, "years old.")

	age_in_10 = input + 10
	age_in_20 = input + 20
	age_in_30 = input + 30

	print(f"In 10 years, you'll be {age_in_10} years old.")
	print(f"In 20 years, you'll be {age_in_20} years old.") 
	print(f"In 30 years, you'll be {age_in_30} years old.")
except ValueError:
	print("ERROR: Careful pass a number!")