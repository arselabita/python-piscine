#!/usr/bin/env python3

def array_of_names(persons):
	lst = list()
	for key, value in persons.items():
		name_lst = key + " " + value
		lst.append(name_lst.title())
	return lst

persons = {
	"jean": "valjean",
	"grace": "hopper",
	"xavier": "niel",
	"fifi": "brindacier"
}

print(array_of_names(persons))