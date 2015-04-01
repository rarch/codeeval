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
        print line.rstrip('\n').lower()

if __name__ == "__main__":
    main()