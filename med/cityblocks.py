#!/usr/bin/env python

import sys
def flyover(strts,aves):
    slope=float(max(aves))/float(max(strts))

    count=0
    for strt in xrange(len(strts)-1):
        for ave in xrange(len(aves)-1):
            if max(strts[strt],aves[ave]/slope)<min(strts[strt+1],aves[ave+1]/slope):
                count+=1
    return count

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        getVals = lambda x:map(int,x.translate(None,'()').split(','))
        [strts,aves]=map(getVals,line.split())
        print flyover(strts,aves)

if __name__ == "__main__":
    main(sys.argv[1])