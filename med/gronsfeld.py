#!/usr/bin/env python

import sys

VOCAB=list(" !\"#$%&'()*+,-./0123456789:<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

def gronsfeld(msg,keys,reverse=False):
    res=''
    if reverse: keys=map(lambda x:-x,keys) # going bkwd if reverse
    for ind in xrange(len(msg)): # go through message
        shift=keys[ind%len(keys)] # shift by the int in keys
        # find char and shift, loop if exceed length of alphabet
        res+=VOCAB[(VOCAB.index(msg[ind])+shift)%len(VOCAB)]
    return res

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        # edge case where line ended in ' '
        lines = [line.strip('\n') for line in f_in if line.rstrip()]

    for line in lines:
        [nums,data]=line.split(';')
        res = gronsfeld(data,map(int,nums),True) # reverse gronsfeld
        assert len(res)==len(data)
        print res

if __name__ == "__main__":
    main(sys.argv[1])