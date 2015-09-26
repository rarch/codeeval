#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.rstrip(): continue
    # 'test' represents the test case, do something with it
    x1,y1,x2,y2 = map(int,test.split())

    if (x1, y1) == (x2, y2):
        res = 'here'
    else:    
        if y2 > y1:
            res = 'N'
        elif y2 < y1:
            res = 'S'
        else:
            res = ''

        if x2 > x1:
            res = res + 'E'
        elif x2 < x1:
            res = res + 'W'

    print res

test_cases.close()