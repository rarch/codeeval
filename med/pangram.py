#!/usr/bin/env python

import sys
from string import lowercase as lowers

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        absent = [c for c in lowers if c not in line]
        print ''.join(absent) if absent else "NULL"

if __name__ == "__main__":
    main(sys.argv[1])