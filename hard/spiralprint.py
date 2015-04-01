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
    # rotate counterclockwise by reversing the transpose
    return list(reversed(zip(*grid)))

def clockwisein(grid):
    # add first row, then recurse on rotation
    return list(grid[0]) + clockwisein(rotCCW(grid[1:])) if grid else []

def doublelist(col,data):
    data = data.strip().split()
    # return [[data[i+j*r] for i in xrange(c)] for j in xrange(r)]
    return [data[ind:ind+col] for ind in xrange(0,len(data),col)]

def main():
    # read file
    lines = []
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    for line in lines:
        _,c,data=line.split(';')
        # get columns
        col = int(c)

        grid = doublelist(col,data)
        print " ".join(clockwisein(grid))

if __name__ == "__main__":
    main()