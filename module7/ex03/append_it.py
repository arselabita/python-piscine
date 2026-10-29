#!/usr/bin/env python3

import sys

if len(sys.argv) - 1 < 1:
	print("none")
	sys.exit(1)

str = sys.argv
for s in str[1:]:
	ism_index = s.find('ism')
	if ism_index > 0:
		continue
	else:
		c=s+"ism"
		print(c)