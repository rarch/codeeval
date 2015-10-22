#!/usr/bin/env python

import sys

def burrowsWheeler(line):
    length=len(line)
    res,temp=[],line
    for _ in xrange(length):
        res.append(temp)
        temp=temp[-1]+temp[:-1]
    res.sort()
    return ''.join([line[-1] for line in res])

def reverseBW(encoded,end='$'):
    matrix = ['']*len(encoded)
    for _ in encoded:
        matrix = sorted(i+j for i,j in zip(encoded, matrix))
    for elt in matrix:
        if elt[-1]==end: return elt
    return None

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]
    
    for line in lines:
        print reverseBW(line.rstrip('|'))

if __name__ == "__main__":
    main(sys.argv[1])