#!/usr/bin/env python

import sys

LIM=10

def next(state,rows,cols):
    next=[]
    for row in xrange(rows):
        next+=[""]
        for col in xrange(cols):
            count=0
            for y in xrange(max(0,row-1),min(row+2,rows)):
                for x in xrange(max(0,col-1),min(col+2,cols)):
                    if ((x!=col) or (y!=row)) and '*'==state[y][x]: count+=1
            next[-1]+=('*' if 3==count or (2==count and '*'==state[row][col]) else '.')
    return next

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        state = [line.strip() for line in f_in if line.rstrip()]

    rows,cols=len(state),len(state[0])
    for _ in xrange(LIM):
        state=next(state,rows,cols)
    print '\n'.join(state)

if __name__ == "__main__":
    main(sys.argv[1])