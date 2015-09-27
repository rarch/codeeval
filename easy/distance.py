#!/usr/bin/env python

import sys
from math import sqrt
from string import translate

def distance(x1,y1,x2,y2):
    return int(sqrt((x2-x1)**2 + (y2-y1)**2))

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.rstrip(): continue
    # 'test' represents the test case, do something with it
    x1,y1,x2,y2 = [int(val) for val in test.translate(None,'(,)').split()]
    print distance(x1,y1,x2,y2)

test_cases.close()