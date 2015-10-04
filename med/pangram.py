#!/usr/bin/env python

import sys
from string import lowercase as lowers

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        absent,line = [],line.lower()
        for char in lowers:
            if char not in line:
                absent+=char
        print ''.join(absent) if absent else "NULL"

if __name__ == "__main__":
    main(sys.argv[1])