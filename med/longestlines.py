#!/usr/bin/env python

import sys

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

def main():
    # read file
    lines = []
    with open(sys.argv[1]) as f:
        nlines = int(f.readline())
        lines = f.read().splitlines()

    lines.sort(cmp=lambda x,y:len(y)-len(x))

    print "\n".join(lines[0:nlines])

if __name__ == "__main__":
    main()