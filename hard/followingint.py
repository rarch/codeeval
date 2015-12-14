#!/usr/bin/env python

import sys
from itertools import permutations

def getNext(digs,val):
    perms = [p for p in permutations(digs)]
    perms = sorted(set([int(''.join(p)) for p in perms]))

    if val==perms[-1]:
        return getNext(['0']+digs,val)
    else:
        return perms[perms.index(val)+1]

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]
    # raise Exception('\n'.join(lines))

    for line in lines:
        digs,val=sorted(line),int(line)
        print getNext(digs,val)

if __name__ == "__main__":
    main(sys.argv[1])