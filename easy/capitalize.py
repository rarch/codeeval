#!/usr/bin/env python

import sys
from string import ascii_lowercase as lowercase

def capitalize(line):
    last,res = ' ',''
    for char in line:
        if ' '==last and char in lowercase:
            res = res + chr(ord(char)-32)
        else: res = res + char
        last = char
    return res

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.rstrip(): continue
    # 'test' represents the test case, do something with it
    print capitalize(test.rstrip())

test_cases.close()