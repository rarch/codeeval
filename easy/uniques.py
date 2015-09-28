#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it
    res = []
    vals = map(int,test.split(','))

    for val in vals:
        if not val in res:
            res.append(val)

    print ','.join(map(str,res))

test_cases.close()