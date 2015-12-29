#!/usr/bin/env python

import sys

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        n=[int(c) for c in line.replace(' ','')]
        tot=sum([val*(2-ind%2) for ind,val in enumerate(n)])
        print 'Fake' if tot%10 else 'Real'

if __name__ == "__main__":
    main(sys.argv[1])