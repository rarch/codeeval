#!/usr/bin/env python

import sys

SUBS = {0:', yeah!',\
            1:', this is crazy, I tell ya.',\
            2:', can U believe this?',\
            3:', eh?',\
            4:', aw yea.',\
            5:', yo.',\
            6:'? No way!',\
            7:'. Awesome!'}

REPLACE = '.!?'
ITEMS = len(SUBS)
other = False
count = 0

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it
    res = ''
    for char in test:
        if char not in REPLACE:
            res = res + char
        else:
            if other:
                res = res + SUBS[count%ITEMS]
                count = count+1
            else:
                res = res + char
            other = not other

    print res

test_cases.close()