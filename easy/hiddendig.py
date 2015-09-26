#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.rstrip(): continue
    # 'test' represents the test case, do something with it
    
    test, result = test.strip(),''

    for char in test:
        if char.isdigit():
            result = result + char
        else:
            val = ord(char)
            if val > 96 and val < 107:
                result = result + chr(val-49)

    print result if result else 'NONE'