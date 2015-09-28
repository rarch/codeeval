#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it
    res,last = '',''

    for char in test:
        if char != last:
            res = res + char
        last = char
    print res

test_cases.close()