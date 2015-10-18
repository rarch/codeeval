#!/usr/bin/env python

import sys

AlphaBet=list(" !\"#$%&'()*+,-./0123456789:<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")


# WHY NOT WORKING 100%? ONLY SCORE OF 95
def gronsfeld(text,keys,reverse=False):
    res=''
    if reverse: keys=map(lambda x:-x,keys)
    for ind in xrange(len(text)):
        shift=keys[ind%len(keys)]
        res+=AlphaBet[(AlphaBet.index(text[ind])+shift)%len(AlphaBet)]
    return res

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        [nums,text]=line.split(';')
        print gronsfeld(text,map(int,nums),True)

if __name__ == "__main__":
    main(sys.argv[1])