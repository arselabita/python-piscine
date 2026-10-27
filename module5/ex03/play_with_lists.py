#!/usr/bin/env python3

original_list = [2, 8, 9, 48, 8, 22, -12, 2]
print(f" Original list: {original_list}")
new_list = [num + 2 for num in original_list if num > 5]
no_dup_list = set(new_list)
print(f" New set: {no_dup_list}")