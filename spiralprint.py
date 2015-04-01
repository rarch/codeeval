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

def rotCCW(grid):
    return list(reversed(zip(*grid)))

def clockwisein(grid):
    return list(grid[0]) + clockwisein(rotCCW(grid[1:])) if grid else []

def doublelist(r,c,data):
    data = data.strip().split()
    return [[data[i+j*r] for i in xrange(c)] for j in xrange(r)]

def main():
    # read file
    lines = []
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    for line in lines:
        r,c,data=line.split(';')
        # get dimensions
        r,c = int(r), int(c)

        grid = doublelist(r,c,data)
        print clockwisein(grid)

if __name__ == "__main__":
    main()