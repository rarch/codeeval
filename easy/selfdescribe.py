#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.rstrip(): continue
    # 'test' represents the test case, do something with it

    numstr = str(int(test))

    res = 1
    for ind in xrange(len(numstr)):
        if numstr.count(str(ind)) != int(numstr[ind]):
            res = 0
            break
            
    print res

test_cases.close()