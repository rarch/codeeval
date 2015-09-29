#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it
    words = test.split()
    print ' '.join([word[-1]+word[1:-1:1]+word[0]for word in words])

test_cases.close()