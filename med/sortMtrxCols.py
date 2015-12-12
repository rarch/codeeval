#!/usr/bin/env python

import sys

def row_compare(x,y):
    length=min(len(x),len(y))
    for ind in xrange(length):
        if x[ind] != y[ind]: return x[ind]-y[ind]

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        mtrx=[]
        for row in line.split('|'):
            mtrx.append(map(int,row.strip().split()))

        # transpose for column compare, and retranspose
        mtrx = map(list,zip(*sorted(zip(*mtrx),cmp=row_compare)))
        # delimit and print
        print ' | '.join([' '.join([str(val) for val in row]) for row in mtrx])

if __name__ == "__main__":
    main(sys.argv[1])