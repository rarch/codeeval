#!/usr/bin/env python

import sys

def fizzbuzz(f, b, lim):
    out = ""
    for val in xrange(1,lim+1):
        if (val % f) and (val % b):
            out += str(val)
        else:
            if not (val % f):
                out += "F"
            if not (val % b):
                out += "B"
        out += " "

    print out

def main():
    # read file
    lines = ""
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    #split line into three integers
    parsed = [[int(n) for n in line.split()] for line in lines]

    for vals in parsed:
        fizzbuzz(vals[0], vals[1], vals[2])

if __name__ == "__main__":
    main()