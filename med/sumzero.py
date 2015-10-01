#!/usr/bin/env python

import sys

def allCombos(lst):
    if len(lst)<=1:
        yield lst
        yield []
    else:
        for elt in allCombos(lst[1:]):
            yield [lst[0]]+elt
            yield elt

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it
    lst = map(int, test.strip().split(',') )

    print len([sln for sln in allCombos(lst)
                if (len(sln)==4) and (not sum(sln))])

test_cases.close()