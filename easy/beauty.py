#!/usr/bin/env python

import sys

from operator import __add__ as add

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it

    letters = {}

    for char in test:
        if char.isalpha():
            char = char.lower()
            if char in letters:
                letters[char] = letters[char]+1
            else:
                letters[char] = 1

    letters = sorted(letters.items(), key=lambda (k,v):(v,k),reverse=True)
    letters = [(letters[i][0],letters[i][1],26-i) for i in xrange(len(letters))]
    
    print reduce(add,map(lambda x:x[1]*x[2],letters),0)

test_cases.close()