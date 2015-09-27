#!/usr/bin/env python

import sys

def sumSqDigs(val):
    return sum(map(lambda c:int(c)**2, str(val)))

def isHappy(val, lim=50):
    dct = {val:True}

    while True:
        val = sumSqDigs(val)
        if val == 1:
            return 1
        elif val in dct:
            return 0
        else:
            dct[val] = True


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.rstrip(): continue
    # 'test' represents the test case, do something with it
    print isHappy(int(test))

test_cases.close()