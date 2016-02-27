#!/usr/bin/env python

import sys

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]
    # raise Exception('\n'.join(lines))

    for line in lines:
        virus,antiv = [x.strip().split() for x in line.split('|')]
        # virus = [int(v,16) for v in virus]
        # antiv = [int(av,2) for av in antiv]
        print sum([int(v,16) for v in virus]) <= sum([int(av,2) for av in antiv])

if __name__ == "__main__":
    main(sys.argv[1])