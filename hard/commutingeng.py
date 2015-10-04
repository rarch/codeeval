#!/usr/bin/env python

import sys,re
from math import sqrt

# ONLY PARTIAL SOLUTION. WHAT IS WRONG WITH THIS?

distance=lambda pt1,pt2: sqrt((pt2[0]-pt1[0])**2+(pt2[1]-pt1[1])**2)
DistanceMatrx = None

def traverse(lengthPathPairs):
    global DistanceMatrx
    keys = set(DistanceMatrx.keys())

    newpaths=[]
    for (length,path) in lengthPathPairs:
        rmdr = keys-set(path)
        if not rmdr:
            return lengthPathPairs
        for point in rmdr:
            newpaths.append(
                (length+DistanceMatrx[path[-1]][point],
                path+[point])
            )

    return traverse(newpaths)

def shortestPath(locs):
    global DistanceMatrx
    DistanceMatrx={a[0]:{b[0]:distance(a[1:],b[1:])
        for b in locs if b!=a}
            for a in locs}

    return min(traverse([(0.0,[1])]),key=lambda x:x[0])

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    coords=re.compile("^(\d+)[^()]*\((-?\d+\.\d+), (-?\d+\.\d+)\)$")

    locs = []
    for line in lines:
        temp = re.match(coords,line).groups()
        locs+=[(int(temp[0]),float(temp[1]),float(temp[2]))]

    (dist,path) = shortestPath(locs)
    print '\n'.join([str(loc) for loc in path])

if __name__ == "__main__":
    main(sys.argv[1])