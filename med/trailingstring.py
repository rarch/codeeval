#!/usr/bin/env python

import sys

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        strA,strB = line.split(',')
        print int(strA[-len(strB):]==strB)

if __name__ == "__main__":
    main(sys.argv[1])