#!/usr/bin/env python3

import sys

if len(sys.argv) - 1 != 1:
	print("none")
	sys.exit(1)

user_input = sys.argv[1]
ask = input("What was the parameter? ")
if ask == user_input:
	print("Good job!")
else:
	print("Nope, sorry...")	
