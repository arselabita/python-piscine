#!/usr/bin/env python3

user_input = input("What you gotta say? : ").strip()
while True:
	print("I got that! ", end="", )
	user_input = input("Anything else? : ")
	if user_input == "STOP":
		break