#!/usr/bin/env python

import sys

# from string import uppercase as uppers
# encoding = dict([(c,str(i+1)) for i,c in enumerate(uppers)])

def countDecodings(myStr):
    # only length 1 or 0, so theres only one option
    if len(myStr) == 1 or len(myStr) == 0: return 1
    count = 0 # no measured options
    numChars = 1

    while True:
        chars = myStr[0:numChars]
        # if run out of chars or val exceeds 26, then fails
        if len(chars)!=numChars or int(chars)>26:break
        # if it works then recurse on subsequent letters
        count = count + countDecodings(myStr[numChars:])
        numChars = numChars + 1 # try adding a character
    return count

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.rstrip(): continue
    # 'test' represents the test case, do something with it
    print countDecodings(test.strip())

test_cases.close()