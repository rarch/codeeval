#!/usr/bin/env python

import sys
from math import sqrt

def distance(pt1,pt2):
    return sqrt( (float(pt1[0])-float(pt2[0]))**2 +
                    (float(pt1[1])-float(pt2[1]))**2 )

def checkSquare(points,eps=0.000001):
    # Do I have four unique points?
    if len(set(points))!=4: return False

    distLst=[]
    for pt1 in points:
        dists=[]
        for pt2 in points:
            if pt1==pt2: continue
            else: dists.append(distance(pt1,pt2))
        distLst.append(sorted(dists))

    for dists in distLst:
        if not ((dists[1]-eps<=dists[0]<=dists[1]+eps) and\
          (dists[2]-eps<=dists[0]*sqrt(2.0)<=dists[2]+eps)):
            return False

    return True

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        ptstrs = map(lambda x:x.translate(None,"() ").split(','),line.split())
        points = map(lambda x:(int(x[0]),int(x[1])),ptstrs)
        print ("true" if checkSquare(points) else "false")

if __name__ == "__main__":
    main(sys.argv[1])