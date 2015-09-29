#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it

    res,upper_flag = '',True
    for char in test.strip():
        if char.islower() and upper_flag:
            res = res + char.upper()
            upper_flag = not upper_flag
        elif char.isupper() and not upper_flag:
            res = res + char.lower()
            upper_flag = not upper_flag
        else:
            if char.isalpha():
                upper_flag = not upper_flag
            res = res + char

    print ''.join(res)

test_cases.close()