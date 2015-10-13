#!/usr/bin/env python

import sys
from math import sqrt

#  0  1   2  3
#  4  5   6  7
#  8  9  10 11
# 12 13  14 15

# def testSubGrids(arr,dim):
#     test = [i for i in xrange(dim*dim)]
#     for i in xrange(dim):
#         print test[i*dim:i*dim+dim]
#     print 'groups'
#     root = int(sqrt(dim))
#     for gridH in xrange(root):
#         for gridV in xrange(root):
#             print [test[subC+root*gridH+dim*(subR+root*gridV)]
#                 for subR in xrange(root) for subC in xrange(root)]

# def checkSubGrids(arr,dim):
#     # THIS DOESN'T WORK, WHY NOT??
#     root=int(sqrt(dim))
#     return all(val in [arr[subC+root*gridH+dim*(subR+root*gridV)]
#       for subR in xrange(root) for subC in xrange(root)
#         for gridH in xrange(root) for gridV in xrange(root)]
#           for val in xrange(1,dim+1))
#     # for gridH in xrange(root):
#     #     for gridV in xrange(root):
#     #         for val in xrange(1,1+dim):
#     #             if val not in [arr[subC+root*gridH+dim*(subR+root*gridV)]
#     #                 for subR in xrange(root) for subC in xrange(root)]:
#     #                     return False
#     # return True

# def checkCols(arr,dim):
#     # for col in xrange(dim):
#     #     print [arr[col+row*dim] for row in xrange(dim)]
#     return all(val in [arr[col+row*dim] for row in xrange(dim) for col in xrange(dim)]
#         for val in xrange(1,1+dim))

# def checkRows(arr,dim):
#     # for row in xrange(0,dim*dim,dim):
#     #     print arr[row:row+dim]
#     return all([val in arr[row:row+dim]
#         for val in xrange(1,1+dim) for row in xrange(0,dim*dim,dim)])
#     # for row in xrange(0,dim*dim,dim):
#     #     for val in xrange(1,dim+1):
#     #         if not val in arr[row:row+dim]:
#     #             return False
#     # return True

# subgrids 0-8: grid#/3 = row and grid#%3 =col

def checkSubGrids(grid,dim):
    if not grid: return False
    root = int(sqrt(dim))
    for subNum in xrange(dim):
        boxR,boxC = subNum/root,subNum%root
        temp = [elt for subR in grid[boxR*root:boxR*root+root]
            for elt in subR[boxC*root:boxC*root+root]]
        if not all(val in temp for val in xrange(1,1+dim)):
            return False
    return True

def checkCols(grid,dim):
    if not grid: return False
    return all(val in col for col in zip(*grid) for val in xrange(1,1+dim))

def checkRows(grid,dim):
    if not grid: return False
    return all(val in row for row in grid for val in xrange(1,1+dim))

def gridify(gridlst,dim):
    if dim*dim!=len(gridlst):
        return None
    grid = []
    for row in xrange(dim):
        grid.append(gridlst[row*dim:row*dim+dim])
    return grid

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        n,data = line.split(';')
        dim = int(n)
        grid = gridify([int(elt) for elt in data.split(',')],dim)
        print checkRows(grid,dim) and checkCols(grid,dim) and checkSubGrids(grid,dim)

        # print dim*dim==len(grid) and 1==min(grid) and dim==max(grid) and\
        #  checkRows(grid,dim) and checkCols(grid,dim) and checkSubGrids(grid,dim)

if __name__ == "__main__":
    main(sys.argv[1])