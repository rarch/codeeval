#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it
    ang = float(test)

    deg = int(ang)
    minute = int(60*(ang-deg))
    sec = int(3600*(ang-deg)-60*minute)

    print str(deg)+'.'+str(minute)+'\''+str(sec)+'"'

test_cases.close()