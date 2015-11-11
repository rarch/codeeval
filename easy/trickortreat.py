#!/usr/bin/env python

import sys
import re

def distribute(vamps,zombs,witchs,houses):
    candies = (3*vamps+4*zombs+5*witchs)*houses
    return candies/(vamps+zombs+witchs)

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        [v,z,w,h] = map(int, re.findall('\d+', line))
        print distribute(v,z,w,h)

if __name__ == "__main__":
    main(sys.argv[1])