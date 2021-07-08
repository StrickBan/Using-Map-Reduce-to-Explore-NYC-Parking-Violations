#!/usr/bin/env python

import sys
import string

curr_key = None
total_frequency = 0
list_make = []
list_color = []

for line in sys.stdin:
    key, frequency = line.strip().split('\t', 1)
    column, term = key.split(', ', 1)
    frequency = int(frequency)

    if curr_key == key:
        total_frequency+= frequency
    else:
        if curr_key:
            curr_column, curr_term = curr_key.split(', ', 1)
            if curr_column == 'vehicle_make':
                list_make.append((curr_term, total_frequency))
            else:
                list_color.append((curr_term, total_frequency))

        curr_key = key
        total_frequency = frequency

if curr_key == key:
    curr_column, curr_term = curr_key.split(', ', 1)
    if curr_column == 'vehicle_make':
        list_make.append((curr_term, total_frequency))
    else:
        list_color.append((curr_term, total_frequency))

list_make = sorted(list_make, key=lambda x: x[0])
list_color = sorted(list_color, key=lambda x: x[0])

for i in range(len(list_make)):
    print('vehicle_make' + '\t' + list_make[i][0] + ', ' + str(list_make[i][1]))

for i in range(len(list_color)):
    print('vehicle_color' + '\t' + list_color[i][0] + ', ' + str(list_color[i][1]))
