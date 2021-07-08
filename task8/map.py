#!/usr/bin/env python

import sys
import os
import string

filename = os.environ.get("mapreduce_map_input_file")

for line in sys.stdin:
    info = line.strip().split(',')
    if info[19]:
        color = info[19]
    else:
        color = 'NONE'
    
    if info[20]:
        make = info[20]
    else:
        make = 'NONE'

    print('vehicle_make' + ', ' + make + '\t' + '1')
    print('vehicle_color' + ', ' + color + '\t'  + '1')
    

