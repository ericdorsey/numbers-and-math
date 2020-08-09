#!/usr/bin/env python3

import string
import itertools
import pprint
import sys

# Uppercase letters of the alphabet as a list
alphabet = [string.ascii_uppercase[i] for i in range(0, 26)]
numbers = [i for i in range(0, 10)]

# All permutations of the alphabet; allowing characters to repeat
perms_alpha = [i for i in itertools.product(alphabet, repeat=3)]

# Number of alphabet permutations
len_perms_alpha = (len(perms_alpha))

# Make a list of strings out of the alphabet permutations
joined_perms_alpha = ["".join(i) for i in perms_alpha]

# All permutations of the numbers; allowing numbers to repeat
perms_nums = [i for i in itertools.product(numbers, repeat=3)]

# Number of numbers permutations
len_perms_nums = (len(perms_nums))

# Make a list of strings out of the numbers permutations
joined_perms_nums = ["".join(map(str, i)) for i in perms_nums]

license_plates = []

# Write them all to a file
with open("plates.txt", "w") as writer:
    #jfor i in range(1, 1000):
    for i in joined_perms_nums:
        for j in joined_perms_alpha:
            #padded_num = f"{i:03}"
            #plate = f"{padded_num}-{j}"
            plate = f"{i}-{j}"
            license_plates.append(plate)
            print(plate)
            #writer.write(f"{plate}\n")

print(f"len_perms_alpha: {len_perms_alpha:,d}") # 17,576
print(f"len_perms_nums: {len_perms_nums:,d}") # 1,000
total_combinations = len_perms_alpha * len_perms_nums
print(f"total_combinations = {total_combinations:,d}") # 17,576,000
