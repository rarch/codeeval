#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it
    x,n = map(int,test.split(','))

    tot = n
    while tot < x:
        tot = tot + n

    print tot

test_cases.close()