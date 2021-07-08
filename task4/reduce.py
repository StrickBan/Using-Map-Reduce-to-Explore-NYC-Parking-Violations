#!/usr/bin/env python

import sys
import string

curr_key = None
total_count = 0

for line in sys.stdin:
    key, value = line.strip().split('\t', 1)
    value = int(value)

    if curr_key == key:
        total_count+= value
    else:
        if curr_key:
            print(curr_key + '\t' + str(total_count))

        curr_key = key
        total_count = value

if curr_key == key:
    print(curr_key + '\t' + str(total_count))

