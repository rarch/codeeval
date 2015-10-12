#!/usr/bin/env python

import sys

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        vals = map(int,line.split())
        length = vals.pop(0)
        rng = set([val for val in xrange(1,length)])

        jumps=[]
        for ind in xrange(length-1):
            jumps.append(abs(vals[ind+1]-vals[ind]))
        print ("Jolly" if rng==set(jumps) else "Not jolly")


if __name__ == "__main__":
    main(sys.argv[1])