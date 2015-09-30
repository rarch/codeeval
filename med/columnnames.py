#!/usr/bin/env python

import sys

from string import uppercase as uppers

def colname(val):
    name = ''
    while val: # while not 0
        mod = (val-1)%26 # -1 because index in uppers
        val = (val-mod)/26 # move on to next character
        name = uppers[mod]+name # add letter to front of name
    return name

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.rstrip(): continue
    # 'test' represents the test case, do something with it
    print colname(int(test.strip()))

test_cases.close()