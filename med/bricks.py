#!/usr/bin/env python

import sys
import re

getInts = re.compile(r'(-?\d+)')

def getSizeHole(holeStr):
    """return size of hole, by two side lengths sorted small to large"""
    match = map(int,(re.findall(getInts,holeStr)))
    return sorted([abs(match[2]-match[0]),abs(match[3]-match[1])])

def getIDSizeBrick(brickStr):
    """extract all ints from brick, save name,\
        and calculate sidelengths, ordered small to larg"""
    match = map(int,re.findall(getInts,brickStr))
    return [match[0],sorted([abs(match[4]-match[1]),\
        abs(match[5]-match[2]),abs(match[6]-match[3])])]

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.rstrip(): continue
    # 'test' represents the test case, do something with it
    hole,bricks = test.strip().split('|')

    bricks = map(lambda x:x.strip(),bricks.split(';'))
    brickData = map(getIDSizeBrick,bricks)

    holeSz = getSizeHole(hole)
    
    itFits = []
    for brick in brickData:
        # if smallest two sides of brick do not exceed sides of hole
        if brick[1][0]<=holeSz[0] and brick[1][1]<=holeSz[1]:
            itFits = itFits + [brick[0]]

    # print - if there are no bricks that fit. else print the ones that fit
    print ','.join([str(name) for name in sorted(itFits)]) if itFits else '-'

test_cases.close()