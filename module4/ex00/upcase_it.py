#!/usr/bin/env python3

try:
	input = input("Give me a word: ").upper()
	print (input)
except ValueError:
	print("ERROR: Careful pass a word!")