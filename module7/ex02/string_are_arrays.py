#!/usr/bin/env python3

import sys

if len(sys.argv) - 1 != 1:
	print("none")
	sys.exit(1)

str = sys.argv[1]
arg_index = str.find('z')
if arg_index < 0:
	print("none")
else:
	print("z")