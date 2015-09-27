#!/usr/bin/env python

import sys

BOARD = [[0]*256]*256

def setRow(i,x):
    BOARD[i] = [x]*len(BOARD[i])
def setCol(j,x):
    for row in BOARD:
        row[j] = x
def queryRow(i):
    return sum(BOARD[i])
def queryCol(j):
    return sum([row[j] for row in BOARD])

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.rstrip(): continue
    # 'test' represents the test case, do something with it
    terms = test.strip().split()
    if terms[0] == 'SetRow':
        setRow(int(terms[1]),int(terms[2]))
    elif terms[0] == 'SetCol':
        setCol(int(terms[1]),int(terms[2]))
    elif terms[0] == 'QueryRow':
        print queryRow(int(terms[1]))
    elif terms[0] == 'QueryCol':
        print queryCol(int(terms[1]))

test_cases.close()