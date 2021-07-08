#!/usr/bin/env python

import sys
import string

curr_key = None
total_amount = 0
total_count = 0

for line in sys.stdin:
    key, value = line.strip().split('\t', 1)
    amount, count = value.split(', ', 1)
    amount = float(amount)
    count = float(count)

    if curr_key == key:
        total_amount+= amount
        total_count+= + count
    else:
        if curr_key:
            average = total_amount/total_count
            print(curr_key + '\t' + "%.2f" %total_amount + ', ' + "%.2f" %average)

        curr_key = key
        total_count = count
        total_amount = amount

if curr_key == key:
    average = total_amount/total_count
    print(curr_key + '\t' + "%.2f" %total_amount + ', ' + "%.2f" %average)

