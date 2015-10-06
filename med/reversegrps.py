#!/usr/bin/env python

import sys

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        lst,grps=line.split(';')
        lst = map(int,lst.split(','))
        grps = int(grps)

        for ind in xrange(0,len(lst),grps):
            temp = lst[ind:ind+grps]
            if len(temp)==grps:
                lst[ind:ind+grps] = temp[::-1]

        print ','.join([str(val) for val in lst])

if __name__ == "__main__":
    main(sys.argv[1])