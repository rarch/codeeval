#!/usr/bin/env python

import sys

#WHAT IS WRONG WITH THIS -- WHY ONLY PARTIAL SOLUTION?

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.rstrip(): continue
    # 'test' represents the test case, do something with it
    [words,chars] = map(str.strip,test.split('|'))

    words = words.split()

    result = ' '.join([word for word in words if
                    all((ch in word) for ch in chars)])

    print result if result else False

test_cases.close()