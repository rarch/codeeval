#!/usr/bin/env python

import sys

tot = 0

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it
    tot = tot + int(test)

print tot

test_cases.close()