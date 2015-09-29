#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it
    data = test.split(':')
    lst = map(int,data[0].strip().split())

    swaps = map(lambda x:map(int,x.split('-')),map(lambda x:x.strip(),data[1].split(',')))
    
    for swap in swaps:
        lst[swap[0]],lst[swap[1]] = lst[swap[1]],lst[swap[0]]

    print ' '.join([str(val) for val in lst])

test_cases.close()