#!/usr/bin/env python

import sys
from string import maketrans,lowercase

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    key=maketrans(lowercase,'uvwxyznopqrstghijklmabcdef')
    for line in lines:
        print line.translate(key)

if __name__ == "__main__":
    main(sys.argv[1])