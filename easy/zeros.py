#!/usr/bin/env python

import sys
from string import replace as strep

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it
    zerostrs,binstr = test.split(),''
    
    for ind in xrange(0,len(zerostrs),2):
        if zerostrs[ind] == '0':
            binstr = binstr + zerostrs[ind+1]
        elif zerostrs[ind] == '00':
            temp = zerostrs[ind+1]
            binstr = binstr + strep(temp,'0','1')

    print int(binstr,2)

test_cases.close()