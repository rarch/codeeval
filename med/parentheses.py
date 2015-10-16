#!/usr/bin/env python

import sys

def checkParens(test,parens={'(':')','{':'}','[':']'}):
    stack=[]
    while test:
        temp=test.pop(0)
        if temp in parens.keys():
            stack.append(temp)
        elif []==stack or (parens[stack.pop()]!=temp):
            return False
    return stack==[]

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        print checkParens(list(line))

if __name__ == "__main__":
    main(sys.argv[1])