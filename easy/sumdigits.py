#!/usr/bin/env python

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it

    print sum(map(int, test.strip()))

test_cases.close()