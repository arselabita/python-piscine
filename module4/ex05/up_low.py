#!/usr/bin/env python3

try:
	user_input = input("Give me a string: ")
	print(user_input.swapcase())
except ValueError:
	print(f"ERROR: {user_input} is not valid.")