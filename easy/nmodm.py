#!/usr/bin/env python
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.rstrip(): continue
    # 'test' represents the test case, do something with it
    n,m = map(int,test.split(','))
    print n-(n/m)*m

test_cases.close()
