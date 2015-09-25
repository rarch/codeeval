#!/usr/bin/env python

import sys

def minshift(lines):
    """return the minimum distance between the x detail and y detail for lines given"""
    minD = -1
    for line in lines:
        if 'Y' == line[0] or 'XY' in line:
            return 0
        dist = line.find('Y') - line.rfind('X') - 1

        if 0 > minD or (dist and (dist < minD)):
            minD = dist

    return minD

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    if test.strip():
        lines = test.split(',')
        print minshift(lines)

test_cases.close()