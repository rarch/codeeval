#!/usr/bin/env python

import sys

FROM_BLDG=6

def countBats(lst,start,end,tol):
    if start>end:# list is sorted, so this means list is done
        return 0
    elif [] == lst:# if list is empty, place and move on
        return 1+countBats([],start+tol,end,tol)
    elif start+tol<=lst[0]:# if can place before first elt, do so
        return 1+countBats(lst,start+tol,end,tol)
    else: # if not, recurse on rest of list
        return countBats(lst[1:],lst[0]+tol,end,tol)

# def countBF(length,tol,locs): # Brute Force, HA HA HA
#     count = 0
#     # counting up, add location if not withing padding of any others
#     for val in xrange(FROM_BLDG,length-FROM_BLDG+1):
#         if all([abs(loc-val)>=tol for loc in locs]):
#             locs=locs+[val]
#             count += 1
#     return count

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        vals = map(int,line.split())
        length,tolerance,bats = vals[0:3]
        locs = vals[3:] if bats and len(vals)>3 else []

        print countBats(locs,FROM_BLDG,length-FROM_BLDG,tolerance)
        # print countBF(length,tolerance,locs)

if __name__ == "__main__":
    main(sys.argv[1])