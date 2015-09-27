#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.rstrip(): continue
    # 'test' represents the test case, do something with it
    longest = max(map(str.strip,test.split(' ')),key=len)

    parts = []
    for ind in xrange(len(longest)):
        parts.append('*'*ind + longest[ind])
    print ' '.join(parts)

test_cases.close()