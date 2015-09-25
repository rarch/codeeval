#!/usr/bin/env python

"""Sample code to read in test cases:

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...

test_cases.close()
"""

import sys

def main():
    lines=[]
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    for line in lines:
        if line:
            # split by commas
            (n,bp1,bp2)=map(int,line.rstrip().split(","))

            print str((1&(n>>(bp1-1))) == (1&(n>>(bp2-1)))).lower()

if __name__ == "__main__":
    main()