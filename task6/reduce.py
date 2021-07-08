#!/usr/bin/env python

import sys
import string

curr_key = None
total_value = 0
toplist = []

for line in sys.stdin:
    key, value = line.strip().split('\t', 1)
    value = int(value)

    if curr_key == key:
        total_value+= value
    else:
        if curr_key:
            toplist.append((curr_key, total_value))

        curr_key = key
        total_value = value

toplist = sorted(toplist, key=lambda x: x[1], reverse = True)

for i in range(0, 20):
    print(toplist[i][0] + '\t' + str(toplist[i][1]))



