#!/usr/bin/env python

import sys,re
from math import sqrt,pi,sin,cos,acos
from itertools import permutations

START = '1' # Specified in problem
EARTH_RAD_KM = 6371.0
DistDict={}

def distancePhiLambda(phi1,lambda1,phi2,lambda2):
    global EARTH_RAD_KM
    return EARTH_RAD_KM*acos(
        sin(phi1)*sin(phi2)+cos(phi1)*cos(phi2)*cos(abs(lambda2-lambda1))
        )

def shortestPath(keys):
    global START
    global DistDict
    keys = [elt for elt in keys if not elt==START]
    nkeys = len(keys)

    minPath,minD = [],sys.maxint

    for journey in permutations(keys):
        dist = DistDict[START][journey[0]]
        for ind in xrange(nkeys-1):
            dist+=DistDict[journey[ind]][journey[ind+1]]
        if dist<minD:
            minD,minPath=dist,[START]+list(journey)

    return minPath

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    coords=re.compile("^(?P<ind>\d+)[^()]*\((?P<lat>-?\d+\.\d+), (?P<lng>-?\d+\.\d+)\)$")

    global DistDict
    keys,points=[],[]
    for line in lines:
        temp = re.match(coords,line)
        keys+=[temp.group('ind')]
        points+=[temp.groups()]

    for ptA in points: # initialize distance dictionary
        for ptB in points:
            name1,name2=ptA[0],ptB[0] # names must be different and not entered
            if (name1!=name2):
                temp=distancePhiLambda(
                    float(ptA[1])*pi/180.0,float(ptA[2])*pi/180.0,
                    float(ptB[1])*pi/180.0,float(ptB[2])*pi/180.0)
                if not name1 in DistDict:
                    DistDict[name1] = {}
                if not name2 in DistDict:
                    DistDict[name2] = {}
                DistDict[name1][name2]=DistDict[name2][name1]=temp

    traversal=shortestPath(keys)
    print '\n'.join([pos for pos in traversal])

if __name__ == "__main__":
    main(sys.argv[1])