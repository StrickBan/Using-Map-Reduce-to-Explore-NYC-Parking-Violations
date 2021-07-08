#!/usr/bin/env python

import sys
import string

curr_key = None
weekend_days = [5, 6, 12, 13, 19, 20, 26, 27]
weekend_total = 0 
weekday_total = 0

for line in sys.stdin:
    key, value = line.strip().split('\t', 1)
    date, count = value.split(',')
    count = float(count)
    date = date.split('-')
    day = int(date[2])

    if curr_key == key:
        if day in weekend_days:
            weekend_total+= count
        else:
            weekday_total+= count
    else:
        if curr_key:
            weekend_average = weekend_total / 8
            weekday_average = weekday_total / 23
            print(curr_key + '\t' + "%.2f" %weekend_average + ', ' + "%.2f" %weekday_average )

        if day in weekend_days:
            weekend_total = count
            weekday_total = 0
        else:
            weekend_total = 0
            weekday_total = count
        curr_key = key

if curr_key == key:
    weekend_average = weekend_total / 8
    weekday_average = weekday_total / 23
    print(curr_key + '\t' + "%.2f" %weekend_average + ', ' + "%.2f" %weekday_average )



