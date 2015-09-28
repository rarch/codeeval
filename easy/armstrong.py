#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it

    val = int(test)
    digs = map(int,list(str(val)))
    length = len(test)

    print val == sum(map(lambda x:x**length,digs))

test_cases.close()