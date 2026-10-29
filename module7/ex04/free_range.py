#!/usr/bin/env python3

import sys

if len(sys.argv) - 1 != 2:
	print("none")
	sys.exit(1)

num1 = int(sys.argv[1])
num2 = int(sys.argv[2]) + 1

array = list(range(num1, num2))
print(array) 