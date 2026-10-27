#!/usr/bin/env python3

try:
	num = round(float(input("Give me a number: ")))
	print(num)
except ValueError:
	print("ERROR: Pass a number!")