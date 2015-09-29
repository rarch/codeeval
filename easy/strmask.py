#!/usr/bin/env python

import sys

def case(val):
    if int(val): return (lambda x:x.upper())
    return (lambda x:x.lower())

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it
    tofmt,fmt = map(str.strip,test.split())

    length = len(tofmt)
    res = ''.join([(case(fmt[ind])(tofmt[ind])) for ind in xrange(length)])
    print res

test_cases.close()