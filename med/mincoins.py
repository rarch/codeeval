#!/usr/bin/env python

import sys

COINS = [5,3,1]

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.rstrip(): continue
    # 'test' represents the test case, do something with it
    val = int(test)

    count = 0
    for coin in COINS:
        count,val = count+val/coin,val-coin*(val/coin)
    print count

test_cases.close()