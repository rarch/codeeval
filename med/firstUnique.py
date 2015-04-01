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

def firstUnique(line):
    count={}
    # get count thru one traversal
    for c in line:
        count[c] = 1 + count.get(c,0)

    # find first non repeating, worst case one traversal
    for c in line:
        if count[c] == 1:
            return c

def main():
    # read file
    lines = []
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    for line in lines:
        if line: #ignore white space
            print firstUnique(line)

if __name__ == "__main__":
    main()