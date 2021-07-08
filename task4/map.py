#!/usr/bin/env python

import sys
import os
import string

filename = os.environ.get("mapreduce_map_input_file")

for line in sys.stdin:
    line = line.strip()
    info = line.split(',')
    if info[16] == 'NY':
        print(info[16] + '\t' + '1')
    else:
        print('Other' + '\t' + '1')
    

