#!/usr/bin/env python

import sys

def check_parens(line):
    open_m,open_M=0,0
    for i,c in enumerate(line):
        if '('==c:
            open_M+=1
            if 0==i or line[i-1]!=':': # check for no colon before
                open_m+=1
        elif ')'==c:
            open_m = max(0,open_m-1)
            if 0==i or line[i-1]!=':': # check for no colon before
                open_M-=1
                if open_M<0:
                    break
    return (0<=open_M and 0==open_m)

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        print 'YES' if check_parens(line) else 'NO'

if __name__ == "__main__":
    main(sys.argv[1])