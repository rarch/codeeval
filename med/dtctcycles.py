#!/usr/bin/env python

import sys

def cycles(lst):
    if (len(lst) == 1): #last elt, so it's a one elt cycle
        return lst[0]
    if lst[0] not in lst[1:]: #elt not in subsequent lst, so move on
        return cycles(lst[1:])
    else: #elt in subsequent list, so capture cycle
        ind = 1
        while lst[ind]!=lst[0]:
            ind += 1
        return lst[0:ind]

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.rstrip(): continue
    # 'test' represents the test case, do something with it
    print ' '.join(cycles(test.strip().split()))
    

test_cases.close()