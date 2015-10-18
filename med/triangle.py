#!/usr/bin/env python

import sys

# Naive approach with backtracking
# def triangle(rows,ind):
#     if len(rows)==1:
#         return rows[0][ind]
#     return rows[0][ind]+max(triangle(rows[1:],ind),triangle(rows[1:],ind+1))

# Dyanmic approach building up from the base
def triangle(rows,ind):
    for row in xrange(len(rows)-1,-1,-1):
        for ind in xrange(len(rows[row])-1):
            maxval = max(rows[row][ind]+rows[row-1][ind],
                         rows[row][ind+1]+rows[row-1][ind])
            rows[row-1][ind]=maxval
    return rows[0][0]

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    print triangle([map(int,line.split()) for line in lines],0)

if __name__ == "__main__":
    main(sys.argv[1])