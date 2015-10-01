#!/usr/bin/env python

import sys

FROM_BLDG=6

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        vals = map(int,line.split())
        length,tolerance,bats = vals[0:3]
        count = 0

        locs = vals[3:] if bats and len(vals)>3 else []
        # counting up, add location if not withing padding of any others
        for val in xrange(FROM_BLDG,length-FROM_BLDG+1):
            if all([abs(loc-val)>=tolerance for loc in locs]):
                locs=locs+[val]
                count += 1

        print count

if __name__ == "__main__":
    main(sys.argv[1])