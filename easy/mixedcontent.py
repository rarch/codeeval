#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it
    items = test.split(',')

    words = 0
    digs = 1
    content=[[],[]]
    for item in items:
        content[digs].append(item) if item.isdigit() \
            else content[words].append(item)

    commajoin = lambda x:','.join(x)
    print '|'.join(map(commajoin,content)).strip('|')

test_cases.close()