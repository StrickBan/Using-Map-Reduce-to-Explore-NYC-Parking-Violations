#!/usr/bin/env python


import sys

curr_value = None
curr_key = None

for line in sys.stdin:
    key, value = line.strip().split('\t', 1)
    
    if curr_key == key:
        count = count + 1
    else:
        if curr_key:
            if count == 1:
                if curr_value != "Other Info":
                    print(curr_key + '\t' + curr_value)

        curr_key = key
        count = 1
        curr_value = value

if count == 1:
    if curr_value != "Other Info":
        print(curr_key + '\t' + curr_value)
