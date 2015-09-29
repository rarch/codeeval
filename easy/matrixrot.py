#!/usr/bin/env python

import sys
from math import sqrt

def rot90cw(matr):
    res = map(list,[row[::-1] for row in zip(*(matr))])
    return res

def list2matr(lst,rowlen):
    return [lst[ind:ind+rowlen] for ind in xrange(0,len(lst),rowlen)]

def matr2list(matr):
    return [col for row in matr for col in row]

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it
    lst = test.split()
    rowlen = int(sqrt(len(lst)))

    print ' '.join(matr2list(rot90cw(list2matr(lst,rowlen))))

test_cases.close()