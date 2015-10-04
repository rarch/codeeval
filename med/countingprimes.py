#!/usr/bin/env python

import sys
from math import sqrt

def eratosthenes(n):
    """sieve of eratosthenes"""
    sieve = [True] * n
    lim = int(sqrt(n))

    for i in xrange(3,lim+1,2):
        if sieve[i]:
            sieve[i*i::i] = [False]*len(sieve[i*i::i])
    return [2]+[i for i in xrange(3,n,2) if sieve[i]]

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        lower,upper=map(int,line.split(','))
        print len([elt for elt in eratosthenes(upper+1) if elt>=lower])

if __name__ == "__main__":
    main(sys.argv[1])