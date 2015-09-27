#!/usr/bin/env python

import sys
from string import ascii_lowercase as lowers
from string import ascii_uppercase as uppers
from string import maketrans,translate

table = maketrans(lowers+uppers,uppers+lowers)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.rstrip(): continue
    # 'test' represents the test case, do something with it
    print test.rstrip('\n').translate(table)

test_cases.close()