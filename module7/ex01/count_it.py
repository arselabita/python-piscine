#!/usr/bin/env python3

import sys

if len(sys.argv) - 1 < 1:
	print("none")
	sys.exit(1)

input_args = sys.argv
count = 0
i = 1
for i, arg in enumerate(input_args[1:], start = 1):
	print(f"{arg}: {len(arg)}")
	count +=1
print(f"parameters: {count}")