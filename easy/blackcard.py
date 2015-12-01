#!/usr/bin/env python

import sys
from operator import methodcaller

def eliminate(lst,n):
    while lst:
        last=lst.pop((n-1)%len(lst))
    return last

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        people,n=map(methodcaller('strip'),line.split('|'))
        people=people.split()
        n=int(n)
        print eliminate(people,n)


if __name__ == "__main__":
    main(sys.argv[1])