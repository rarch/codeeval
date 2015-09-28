#!/usr/bin/env python

import sys

TREE = (30,(8,3,(20,10,29)),52)

def ancestors(val):
    ancs = []
    tree = TREE
    while tree[0] != val:
        ancs.append(tree[0])
        tree = tree[1] if val<tree[0] else tree[2]
        if val == tree:
            break
    ancs.append(val)
    return ancs[::-1]

def firstcommon(xs,ys):
    for x in xs:
        for y in ys:
            if x == y:
                return x
    return None

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it
    val1,val2 = map(int,test.split())
    print firstcommon(ancestors(val1),ancestors(val2))

test_cases.close()
