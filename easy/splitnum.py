#!/usr/bin/env python

import sys
from operator import __add__ as add
from operator import __sub__ as sub

list2int = lambda x: int(''.join(x),10)
poss_opps = {'+':add,'-':sub}

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it
    nums,fmt = test.split(' ')

    fmt = list(fmt)
    todo,term,operands = None,0,[[]]

    for char in fmt:
        if char in poss_opps:
            todo = poss_opps[char]
            term = 1
            operands.append([])
        else:
            operands[term].append(nums[ord(char)-97])

    # run todo function on the operands turned into integers
    print todo(*map(list2int,operands))

test_cases.close()