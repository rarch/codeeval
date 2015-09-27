#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.rstrip(): continue
    # 'test' represents the test case, do something with it

    last,count,res = None,0,''
    for val in map(int,test.split()):
        if last == None:
            last,count = val,1
        elif last == val:
            count = count + 1
        else:
            res = (res + ' ' if res else '') + str(count) + ' ' + str(last)
            last,count = val,1

    res = (res + ' ' if res else '') + str(count) + ' ' + str(last)
    print res

test_cases.close()