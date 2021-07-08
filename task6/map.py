#!/usr/bin/env python

import sys
import os
import string

filename = os.environ.get("mapreduce_map_input_file")

for line in sys.stdin:
    info = line.strip().split(',')
    plate_id = info[14]
    state = info[16]
    print(plate_id + ', ' + state + '\t' + '1')

