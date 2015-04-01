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

#two lists
#empty newline in case of skew sets

import sys

def prettyPrint(shared):
    print ",".join(map(str,shared)) if shared else ""

def intersection(setA,setB):
    shared = []
    for itemA in setA:
        if itemA in setB:
            shared.append(itemA)

    return shared

def main():
    lines=[]
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    for line in lines:
        getNums = lambda x: map(int,x.split(","))
        setA,setB = map(getNums,line.strip().split(";"))

        prettyPrint(intersection(setA,setB))

if __name__ == "__main__":
    main()