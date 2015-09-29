#!/usr/bin/env python

import sys

# NUMS = '12345678'
LTRS = 'abcdefgh'
SIZE = 8

def generateAll(col,row):
    return [(col-2,row-1),(col-2,row+1),(col-1,row-2),(col-1,row+2),\
            (col+1,row-2),(col+1,row+2),(col+2,row-1),(col+2,row+1)]

valid = lambda x:(0<=x[0]<SIZE) and (0<=x[1]<SIZE)
pretty = lambda x:LTRS[x[0]]+str(x[1]+1)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.rstrip(): continue
    # 'test' represents the test case, do something with it
    loc = test.strip()
    myC,myR = LTRS.index(loc[0]),int(loc[1])-1

    lst = [pair for pair in generateAll(myC,myR) if valid(pair)]
    print ' '.join(sorted(map(pretty,lst)))

test_cases.close()