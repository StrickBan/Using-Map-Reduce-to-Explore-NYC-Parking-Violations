#!/usr/bin/env python

import sys
import os
import string

filename = os.environ.get("mapreduce_map_input_file")

for line in sys.stdin:
    info = line.strip().split(',')
    issue_date = info[1]
    violation_code = info[2]
    print(violation_code + '\t' + issue_date + ', ' + '1.00')

