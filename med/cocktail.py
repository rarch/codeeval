#!/usr/bin/env python

import sys

def cocktail(lst,iters=sys.maxint):
    '''
    First sort up, then down, switching pairs of numbers to get the smaller number earlier.
    >>> ' '.join(map(str,cocktail([5,4,9,10,7,3,2,1,6],1)))
    '1 4 5 9 7 3 2 6 10'
    >>> ' '.join(map(str,cocktail([9,8,7,6,5,4,3,2,1],3)))
    '1 2 3 6 5 4 7 8 9'
    '''
    upper=len(lst)-1
    def half_cocktail(start,end,change):
        for i in xrange(start,end,change):
            if lst[i+1]<lst[i]:
                lst[i],lst[i+1]=lst[i+1],lst[i]
    for _ in xrange(iters):
        half_cocktail(0,upper,1)
        half_cocktail(upper-1,-1,-1)
    return lst

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]
    for line in lines:
        line,iters=line.split('|')
        lst = map(int, line.split())
        iters = int(iters)
        print ' '.join(map(str,cocktail(lst,iters)))

if __name__ == "__main__":
    main(sys.argv[1])
    # import doctest
    # doctest.testmod()