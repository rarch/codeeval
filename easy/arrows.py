#!/usr/bin/env python

import sys

arrows = ['>>-->','<--<<']
alen = len(arrows[0])

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it
    count = 0
    for ind in xrange(len(test)-alen+1):
        temp = test[ind:ind+alen]
        if temp in arrows:
            count = count + 1

    print count

test_cases.close()