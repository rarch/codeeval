#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.rstrip(): continue
    # 'test' represents the test case, do something with it

    vals = map(int,test.split(','))
    majority = len(vals)/2+1
    occs,res = {},None

    for val in vals:
        if not val in occs:
            occs[val] = 1
        else:
            occs[val] = occs[val]+1
        if occs[val] >= majority:
            res = val
            break
    print res

test_cases.close()