#!/usr/bin/env python3

import sys

def shrink(word):
	if not word:
		print("none")
	x = slice(0,8)
	return word[x]

def enlarge(word):
	if not word:
		print("none")
	while len(word) < 8:
		word += 'Z'
	return word

if len(sys.argv) -1< 1:
	print("none")
	sys.exit(1)

user_input = sys.argv
for s in user_input[1:]:
	str_len = len(s)
	if str_len > 8:
		print(shrink(s))
	elif str_len < 8:
		print(enlarge(s))
	else:
		print(s)
