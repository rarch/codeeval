#!/usr/bin/env python

import sys

letters = {1000:'M',900:'CM',500:'D',400:'CD',\
            100:'C',90:'XC',50:'L',40:'XL',\
            10:'X',9:'IX',5:'V',4:'IV',1:'I'}
choices = sorted(letters,lambda x,y:y-x)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.rstrip(): continue
    # 'test' represents the test case, do something with it

    val,res = int(test),''

    for diff in choices:
        if val == 0:
            break
        while val >= diff:
            val,res = val - diff, res + letters[diff]
    print res

test_cases.close()