#!/usr/bin/env python

import sys
from math import sqrt

def distance(pntA,pntB,coords=2,precis=4):
    return round(sqrt(sum([(pntB[ind]-pntA[ind])**2 for ind in xrange(coords)])),precis)

def closestPair(points):
    """return distance between two closest points"""
    minD=distance(points[0],points[1])
    length=len(points)
    for pt1 in xrange(length):
        for pt2 in xrange(length):
            if pt1!=pt2:
                dist=distance(points[pt1],points[pt2])
                if dist<minD: minD=dist
    return minD

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    lst,lsts=[],[]
    count=-1
    for line in lines:
        if 0==count: break
        if 1==len(line.split()):
            if lst:
                assert count==len(lst)
                lsts.append(lst)
            count=int(line)
            lst=[]
        else:
            lst.append(map(int,line.split()))

    for lst in lsts:
        print "{0:.4f}".format(closestPair(lst))

if __name__ == "__main__":
    main(sys.argv[1])