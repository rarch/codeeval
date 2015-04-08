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

def linkNext(byFirst,sofar):
    assert sofar
    chmatch = sofar[-1][-1]
    try:
        options = byFirst[chmatch] - set(sofar)
    except KeyError:
        return sofar    
    if not options:
        return sofar
    else:
        alternatives = (linkNext(byFirst,list(sofar)+[word]) for word in options)
        longest = max(alternatives,key = len)
        return longest

def orderWords(words):
    byFirst = {}
    for word in words:
        try:
            byFirst[word[0]].add(word)
        except KeyError:
            byFirst[word[0]] = set([word])
    return byFirst

def getLongest(words):
    byFirst = orderWords(words)
    return max( (linkNext(byFirst,[word]) for word in words), key=len)

def main():
    # read file
    lines = []
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()

    for line in lines:
        if line:
            wordSet = sorted(set(line.strip().lower().split(',')))
            longest = getLongest(wordSet)

            lenl = len(longest)
            print lenl if lenl > 1 else None

if __name__ == "__main__":
    main()