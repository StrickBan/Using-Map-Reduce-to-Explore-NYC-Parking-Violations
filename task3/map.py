#!/usr/bin/env python

import sys
import os
import string

filename = os.environ.get("mapreduce_map_input_file")

for line in sys.stdin:
    info = line.strip().split(',')
    key = info[2]
    if info[12]:
        amount_due = float(info[12])
    else:
        amount_due = float(0.00)
    print(key + '\t' + str(amount_due) + ', ' + '1.00')

