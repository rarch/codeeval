#!/usr/bin/env python

import sys

def interruptedBubble(lst,iters):
    changed=True
    count=0
    while changed and (count<iters):
        changed=False
        for ind in xrange(len(lst)-1):
            if lst[ind]>lst[ind+1]:
                lst[ind],lst[ind+1],changed=lst[ind+1],lst[ind],True
        count+=1
    return lst

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        items,nstr=line.split(' | ')
        lst=map(int,items.split())
        reps=int(nstr)

        print ' '.join([str(elt) for elt in interruptedBubble(lst,reps)])

if __name__ == "__main__":
    main(sys.argv[1])