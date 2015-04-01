#!/usr/bin/env python

import sys

"""Sample code to read in test cases:

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...

test_cases.close()
"""

def fizzbuzz(f, b, lim):
    out = ""
    for val in xrange(1,lim+1):
        if (val % f) and (val % b):
            out += str(val)
        else:
            if not (val % f):
                out += "F"
            if not (val % b):
                out += "B"
        out += " "

    print out

def main():
    # read file
    lines = ""
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    #split line into three integers
    parsed = [[int(n) for n in line.split()] for line in lines]

    for vals in parsed:
        fizzbuzz(vals[0], vals[1], vals[2])

if __name__ == "__main__":
    main()