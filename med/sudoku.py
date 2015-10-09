#!/usr/bin/env python

import sys
from math import sqrt

#  0  1   2  3
#  4  5   6  7
#  8  9  10 11
# 12 13  14 15

def checkSubGrids(arr,dim):
    root=int(sqrt(dim))
    # DOES NOT WORK. WHY NOT?
    # return all(val in [arr[col+hrz*root+(row+vrt*root)*dim] for hrz in xrange(root)
    #   for vrt in xrange(root) for row in xrange(root) for col in xrange(root)]
    #     for val in xrange(1,dim+1))

    # examine all root*root subgrids shifting over by hrz and down by vrt
    for hrz in xrange(root):
      for vrt in xrange(0,dim,root):
        for val in xrange(1,dim+1):
            if val not in [arr[col+(row+vrt)*dim+hrz*root]
              for row in xrange(root) for col in xrange(root)]:
                return False
    return True

def checkCols(arr,dim):
    return all(val in [arr[col+dim*row] for col in xrange(dim) for row in xrange(dim)]
        for val in xrange(1,dim+1))

def checkRows(arr,dim):
    return all([val in arr[row:row+dim]
        for val in xrange(1,dim+1) for row in xrange(0,dim*dim,dim)])

    # for row in xrange(0,dim*dim,dim):
    #     for val in xrange(1,dim+1):
    #         if not val in arr[row:row+dim]:
    #             return False
    # return True

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        n,data = line.split(';')
        dim = int(n)
        grid = [int(elt) for elt in data.split(',')]
        print checkRows(grid,dim) and checkCols(grid,dim) and checkSubGrids(grid,dim)

if __name__ == "__main__":
    main(sys.argv[1])