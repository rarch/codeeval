#!/usr/bin/env python

import sys

from operator import __add__ as add

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it
    parsed = map(int,test.split())
    # friends = parsed[0]
    locs = sorted(parsed[1:])
    minadd,maxadd=locs[0],locs[-1]

    dists = []

    for house in xrange(minadd,maxadd+1):
        dists.append(reduce(add,map(lambda loc:abs(loc-house),locs),0))

    print min(dists)

test_cases.close()