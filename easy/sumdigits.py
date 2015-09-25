#!/usr/bin/env python

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    data = test.strip()
    if data:
        print sum(map(int, data))

test_cases.close()