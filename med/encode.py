#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.rstrip(): continue
    # 'test' represents the test case, do something with it
    mystr = test.strip()

    # go through string of digits
    # every one- or two-digit number must be between 1 and 26
    # only one choice as long as not preceeded or followed by something
    #   that could turn into two digits; else one more choice
    length = len(mystr)
    choices = 1
    for ind in xrange(length):
        if ind + 1 < length and 1<=int(mystr[ind:ind+1])<=26:
            choices = choices + 1

    print choices

test_cases.close()