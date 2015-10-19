#!/usr/bin/env python

import sys

Romans={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

def compute(components):
    global Romans
    res=0

    # if last roman< this roman
    #   subtract last
    # else add it, and this is last

    last=components.pop(0)
    tempR=Romans[last[1]]

    while components:
        temp=components.pop(0)
        lastR,tempR=tempR,Romans[temp[1]]
        if lastR<tempR:
            res-=lastR*last[0]
        else:
            res+=lastR*last[0]
        last=temp
        
    lastR=tempR
    res+=lastR*last[0]
    return res

def aromatic(numstr):
    components=[]
    for ind in xrange(0,len(numstr),2):
        components+=[(int(numstr[ind]),numstr[ind+1])]
    return compute(components)

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        print aromatic(line)

if __name__ == "__main__":
    main(sys.argv[1])