#!/usr/bin/env python

import sys

def checkSums(lst,target):
    res=[]
    while lst:
        scnd = lst.pop()
        for ind in xrange(len(lst)):
            if lst[ind]+scnd==target:
                frst=lst.pop(ind)
                res+=[str(frst)+','+str(scnd)]
                break
    return res

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        lst,target = line.split(';')
        lst,target = map(int,lst.split(',')),int(target)

        res=checkSums(lst,target)
        print ';'.join(res) if res else 'NULL'

if __name__ == "__main__":
    main(sys.argv[1])