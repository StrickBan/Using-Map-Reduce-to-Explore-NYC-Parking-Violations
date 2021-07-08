#!/usr/bin/env python

import sys
import string

curr_key = None
total_value = 0
greatest_value = 0

for line in sys.stdin:
    key, value = line.strip().split('\t', 1)
    value = int(value)

    if curr_key == key:
        total_value+= value
    else:
        if total_value > greatest_value:
            greatest_value = total_value
            greatest_key = curr_key

        curr_key = key
        total_value = value

print(greatest_key + '\t' + str(greatest_value))

