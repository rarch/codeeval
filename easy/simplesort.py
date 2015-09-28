#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it
    vals = map(float,test.split())
    print ' '.join(map(lambda val:"{0:.3f}".format(val),sorted(vals)))

test_cases.close()