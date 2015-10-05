#!/usr/bin/env python

import sys
from math import sqrt

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines[1:]:
        x = int(line)
        count=0
        for a in xrange(int(sqrt(x))+1):
            b=sqrt(x-a*a)
            if b==int(b): # working with integers
                if a==b: count+=2 # only enters once, but count twice and div/2
                else: count+=1 # enters twice (a+b,b+a), so count once, and div/2
        print count/2

if __name__ == "__main__":
    main(sys.argv[1])