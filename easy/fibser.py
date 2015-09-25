#!/usr/bin/env python

import sys

known_fib = {0:0, 1:1}

def fib(n):
    if n in known_fib:
        return known_fib[n]
    result = fib(n-1)+fib(n-2)
    known_fib[n] = result
    return result

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if test.strip():
    # 'test' represents the test case, do something with it
        print fib(int(test))

test_cases.close()