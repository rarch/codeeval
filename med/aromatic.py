#!/usr/bin/env python

import sys

Romans={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

def aromatic2int(numstr):
    global Romans
    res=0

    lastC,lastR=int(numstr[0]),Romans[numstr[1]]
    for ind in xrange(2,len(numstr),2):
        tempC,tempR=int(numstr[ind]),Romans[numstr[ind+1]]
        if lastR<tempR: res-=lastC*lastR
        else: res+=lastC*lastR
        lastC,lastR=tempC,tempR
    res+=lastC*lastR
    
    return res

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        print aromatic2int(line)

if __name__ == "__main__":
    main(sys.argv[1])