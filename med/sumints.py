#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it
    lstOfInts = map(int, test.strip().split(',') )
    length = len(lstOfInts)

    print max([sum(lstOfInts[ind:jnd]) # capture sum of substring
                for ind in xrange(length+1) # for start moving from lst[0] to lst[-1]
                    for jnd in xrange(ind+1,length+1)]) # for end moving from ind+1
                                                        # to lst[-1]

test_cases.close()