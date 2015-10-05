#!/usr/bin/env python

import sys

#O(N) space for length of line; +1 for sorting it, is that technically Constant?
#O(NlogN) time to sort, but O(N) time to go through list after sorting
# TOTAL is O(N) space, O(NlogN) time
# or I don't understand this?

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        _,line=line.split(';')
        line=sorted(line.split(','))

        temp = line[0]
        for val in line[1:]:
            if val==temp:
                print val
                break
            temp = val

if __name__ == "__main__":
    main(sys.argv[1])