#!/usr/bin/env python3

def find_the_redheads(dupont_family):
	lst = list()
	for keys, values in dupont_family.items():
		if values == "red":
			lst.append(keys)
	return lst

dupont_family = {
	"florian": "red",
	"marie": "blond",
	"virginie": "brunette",
	"david": "red",
	"franck": "red"
}

print(find_the_redheads(dupont_family))