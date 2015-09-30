#!/usr/bin/env python

import sys

def isInRect(vert,rect):
    return rect[0]<=vert[0]<=rect[2] and rect[3]<=vert[1]<=rect[1]

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.rstrip(): continue
    # 'test' represents the test case, do something with it
    lxa,uya,rxa,lya,lxb,uyb,rxb,lyb = map(int,test.split(','))
    # rectA = [(lxa,uya),(rxa,uya),(rxa,lya),(lxa,lya)]
    # rectB = [(lxb,uyb),(rxb,uyb),(rxb,lyb),(lxb,lyb)]
    rectA = [lxa,uya,rxa,lya]
    rectB = [lxb,uyb,rxb,lyb]

    overlap = any([ isInRect((rectB[0],rectB[1]),rectA),\
                    isInRect((rectB[2],rectB[1]),rectA),\
                    isInRect((rectB[2],rectB[3]),rectA),\
                    isInRect((rectB[0],rectB[3]),rectA),\
                    isInRect((rectA[0],rectA[1]),rectB),\
                    isInRect((rectA[2],rectA[1]),rectB),\
                    isInRect((rectA[2],rectA[3]),rectB),\
                    isInRect((rectA[0],rectA[3]),rectB) ])

    print overlap

test_cases.close()