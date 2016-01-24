#!/usr/bin/env python

import sys

def stupid(lst,iters=sys.maxint):
    '''
    First sort up, then down, switching pairs of numbers to get the smaller number earlier.
    >>> ' '.join(map(str,stupid([4,3,2,1],1)))
    '3 4 2 1'
    >>> ' '.join(map(str,stupid([5,4,3,2,1],2)))
    '4 3 5 2 1'
    '''
    upper,flag=len(lst)-1,False
    for _ in xrange(iters):
        if flag: return lst
        for ind in xrange(upper):
            if lst[ind]>lst[ind+1]:
                lst[ind],lst[ind+1]=lst[ind+1],lst[ind]
                break
            elif ind==upper-1: flag=True
    return lst

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]
    for line in lines:
        lst,iters=map(lambda x,y:x(y),
            [(lambda l:map(int,l.split())),int],line.split('|'))
        print ' '.join(map(str,stupid(lst,iters)))

if __name__ == "__main__":
    main(sys.argv[1])
    # import doctest
    # doctest.testmod()