#!/usr/bin/env python

# import sys
# test_cases = open(sys.argv[1], 'r')
# for test in test_cases:
#     # ignore test if it is an empty line
#     if not test.rstrip(): continue
#     # 'test' represents the test case, do something with it

# test_cases.close()

def printLine(n,lim):
    res = ''
    for i in xrange(1,lim+1):
        res = res + str(n*i).rjust(4,' ')
    print res

def printTable(lim):
    for i in xrange(1,lim+1):
        printLine(i,lim)

printTable(12)