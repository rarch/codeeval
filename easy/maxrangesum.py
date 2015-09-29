#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it
    length,data = test.split(';')
    length = int(length)
    data = map(int,data.strip().split())
    total = len(data)

    maxrange = 0
    for ind in xrange(0,total-length+1):
        temp = sum(data[ind:ind+length])
        if temp > maxrange:
            maxrange = temp

    print maxrange

test_cases.close()