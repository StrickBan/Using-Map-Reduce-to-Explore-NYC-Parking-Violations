#!/usr/bin/env python


import sys

count = 0
curr_key = None

for line in sys.stdin:
    key, value = line.strip().split('\t', 1)
    value = int(value)
    
    if curr_key == key:
        count = count + value
    else:
        if curr_key:
            print(curr_key + '\t' + str(count))
        curr_key = key
        count = value

if curr_key == key:
    print(curr_key + '\t' + str(count))
