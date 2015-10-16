#!/usr/bin/env python

import sys

def pascal(line,lines=None):
    if not lines: lines = [[1]]
    if line<1: return [[]]
    if line==1:
        return lines
    prev=lines[-1]
    res=[x+y for x,y in zip([0]+prev,prev+[0])]
    return pascal(line-1,lines+[res])

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        print ' '.join([str(elt) for lst in pascal(int(line))
            for elt in lst])

if __name__ == "__main__":
    main(sys.argv[1])