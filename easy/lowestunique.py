#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it

    vals = map(int,test.split())
    occs = {}

    for val in vals:
        if not val in occs:
            occs[val] = 1
        else:
            occs[val] = occs[val]+1

    uniques = [k for (k,v) in occs.items() if v==1]
    
    if len(uniques) == 0:
        print 0
    else:
        print vals.index(min(uniques))+1

test_cases.close()