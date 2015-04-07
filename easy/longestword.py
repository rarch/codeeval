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
        lines = f.read().splitlines()

    for line in lines:
        if line:
            maxLength = 0
            longestWord = None

            for word in line.split():
                if len(word) > maxLength:
                    maxLength = len(word)
                    longestWord = word

            print longestWord

if __name__ == "__main__":
    main()