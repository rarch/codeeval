#!/usr/bin/env python

import sys

def timeStr2Val(tStr):
    temp = map(int,tStr.split(':'))
    return 3600*temp[0] + 60*temp[1] + temp[2]

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.rstrip(): continue
    # 'test' represents the test case, do something with it
    timeLst = test.split()
    print ' '.join([item for item in \
        sorted(timeLst,key=lambda t:timeStr2Val(t),reverse=True)])

test_cases.close()