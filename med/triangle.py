#!/usr/bin/env python

import sys

def triangle(rows,ind):
    if len(rows)==1:
        return rows[0][ind]
    return rows[0][ind]+max(triangle(rows[1:],ind),triangle(rows[1:],ind+1))

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    print triangle([map(int,line.split()) for line in lines],0)

if __name__ == "__main__":
    main(sys.argv[1])