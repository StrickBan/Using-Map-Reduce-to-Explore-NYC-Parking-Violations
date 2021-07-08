#!/usr/bin/env python

import sys
import os
import string


filename = os.environ.get("mapreduce_map_input_file")

for line in sys.stdin:
    if "parking" in filename:
        info = line.strip().split(',')
        key = info[0]
        plate_id = info[14]
        violation_precinct = info[6] 
        violation_code = info[2]
        issue_date = info[1]
        print(key + '\t' + plate_id + ',' + violation_precinct + ',' + violation_code + ',' + issue_date)
    elif "open" in filename:
        info = line.strip().split(',')
        key = info[0]
        print(key + '\t' + "Other Info")
