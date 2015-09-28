#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it
    chars,keystring = test.split('|')
    indices = map(int,keystring.strip().split())

    print ''.join(chars[index-1] for index in indices)
    
test_cases.close()