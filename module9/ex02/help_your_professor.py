#!/usr/bin/env python3

def average(class_avg):
	total = 0
	for values in class_avg.values():
		total += values
	avg = total / len(class_avg)

	return avg 

class_3B = {
	"marine": 18,
	"jean": 15,
	"coline": 8,
	"luc": 9
}
class_3C = {
	"quentin": 17,
	"julie": 15,
	"marc": 8,
	"stephanie": 13
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")