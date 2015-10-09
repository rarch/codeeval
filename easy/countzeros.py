#!/usr/bin/env python

import sys

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        [numzeros,lim] = map(int,line.split())
        count=0
        for val in xrange(1,lim+1):
            if numzeros=="{0:b}".format(val).count('0'):
                count+=1
        print count

if __name__ == "__main__":
    main(sys.argv[1])