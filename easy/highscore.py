#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it
    getInts = lambda x:map(int,x.strip().split())
    byPlayer = map(getInts,test.split('|'))

    byScore = zip(*byPlayer)
    print ' '.join(map(lambda x:str(max(x)),byScore))

test_cases.close()