#!/usr/bin/env python

import sys

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        val = str(int(line))
        count=0

        while val != val[::-1] and count<100:
            val,count = str(int(val)+int(val[::-1])),count+1

        print ' '.join([str(count),val])
        
if __name__ == "__main__":
    main(sys.argv[1])