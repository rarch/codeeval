#!/usr/bin/env python

import sys

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        stack,res = [int(elt) for elt in line.split()],[]
        while stack:
            res=res+[str(stack.pop())]
            if stack:
                stack.pop()
        print ' '.join(res)

if __name__ == "__main__":
    main(sys.argv[1])