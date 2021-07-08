#!/usr/bin/env python

import sys
import os
import string

for line in sys.stdin:
    info = line.strip().split(',')
    key = info[2]
    value = 1
    print(key + '\t' + str(value))

