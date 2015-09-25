#!/usr/bin/env python

import sys

def abridge(line, suffix):
    line = line[:40]
    if ' ' in line:
        line = line[:line.rfind(' ')]
    return line+suffix

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    test = test.rstrip()
    if len(test) > 55:
        test = abridge(test, '... <Read More>')
    print test

test_cases.close()