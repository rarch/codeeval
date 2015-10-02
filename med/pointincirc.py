#!/usr/bin/env python

import sys
import re

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    vals = re.compile("([-+]?[0-9]*\.?[0-9]+)")

    for line in lines:
        lst = map(float,re.findall(vals,line))
        ctr,pnt,rad = (lst[0],lst[1]),(lst[3],lst[4]),lst[2]

        print 'true' if (pnt[0]-ctr[0])**2+(pnt[1]-ctr[1])**2<=rad**2 else 'false'

if __name__ == "__main__":
    main(sys.argv[1])