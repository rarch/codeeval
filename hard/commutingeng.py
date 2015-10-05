#!/usr/bin/env python

import sys,re
from math import sqrt,pi,sin,cos,acos
from itertools import permutations

START = '1' # Specified in problem
EARTH_RAD_MILES = 3959

# def distance(ptA,ptB):  # THIS IS CARTESIAN DISTANCE FOR 2D GRAPHS -- YOU IDIOT --
#                         # YOU'RE WORKING WITH AN APPROXIMATE SPHERE
#     return sqrt( (ptB[0]-ptA[0])**2 +
#                 (ptB[1]-ptA[1])**2 )

def roundDistance(ptA,ptB):
    global EARTH_RAD_MILES
    phiA,thetaA=ptA[0]*pi/180.0,ptA[1]*pi/180.0
    phiB,thetaB=ptB[0]*pi/180.0,ptB[1]*pi/180.0
    return EARTH_RAD_MILES*acos(
        sin(phiA)*sin(phiB)*cos(thetaA-thetaB)+cos(phiA)*cos(phiB)
        )

# DistanceMatrx = None
# def traverse(lengthPathPairs):
#     global DistanceMatrx
#     keys = set(DistanceMatrx.keys())
#     newpaths=[]
#     for (length,path) in lengthPathPairs:
#         rmdr = keys-set(path)
#         if not rmdr:
#             return lengthPathPairs
#         for point in rmdr:
#             newpaths.append(
#                 (length+DistanceMatrx[path[-1]][point],
#                 path+[point])
#             )
#     return traverse(newpaths)
# def shortestPath(locs):
#     global DistanceMatrx
#     DistanceMatrx={a[0]:{b[0]:roundDistance(a[1:],b[1:])
#         for b in locs if b!=a}
#             for a in locs}
#     return min(traverse([(0.0,[1])]),key=lambda x:x[0])

def shortestPath_rev(locDict):
    global START
    pathLength,minPath=sys.maxint,[]
    points=list(locDict.keys())
    del points[points.index(START)]
    print points
    nPoints = len(points)
    for traversal in permutations(points):
        temp = roundDistance(locDict[START],locDict[traversal[0]])
        for ind in xrange(len(traversal)-1):
            temp+=roundDistance(locDict[traversal[ind]],
                            locDict[traversal[ind+1]])
        if temp<pathLength:
            pathLength,minPath=temp,[START]+list(traversal)
    return minPath

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    coords=re.compile("^(\d+)[^()]*\((-?\d+\.\d+), (-?\d+\.\d+)\)$")

    locs = {}
    for line in lines:
        temp = re.match(coords,line).groups()
        locs[temp[0]]=(float(temp[1]),float(temp[2]))
    traversal=shortestPath_rev(locs)
    print '\n'.join([val for val in traversal])

    # locs = []
    # for line in lines:
    #     temp = re.match(coords,line).groups()
    #     locs+=[(int(temp[0]),float(temp[1]),float(temp[2]))]
    # (dist,path) = shortestPath(locs)
    # print '\n'.join([str(loc) for loc in path])

if __name__ == "__main__":
    main(sys.argv[1])