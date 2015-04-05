#!/usr/bin/env python

import sys
import re

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
        lines = f.readlines()

    # use re to get list and idx
    for line in lines:
        m = re.match("^(?P<charlist>([a-zA-Z]\s)*)(?P<idx>\d+).*$",line)
        idx = int(m.group("idx"))
        charlist = m.group("charlist").strip().split()

        # print mth to last for valid entry
        if idx<=len(charlist):
            print charlist[-idx]

if __name__ == "__main__":
    main()