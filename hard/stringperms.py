#!/usr/bin/env python

import sys
from itertools import permutations

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.rstrip(): continue
    # 'test' represents the test case, do something with it
    perms = [''.join(perm) for perm in permutations(test.strip())]
    print ','.join(sorted(perms))

test_cases.close()