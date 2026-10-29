#!/usr/bin/env python3

import sys

def downcase_it(str):
	return str.lower()

if len(sys.argv) -1 < 1:
	print("none")
	sys.exit(1)

user_input = sys.argv
for s in user_input:
	print(downcase_it(s))