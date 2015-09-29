#!/usr/bin/env python

import sys

def timeStr2Val(tStr):
    temp = map(int,tStr.split(':'))
    return 3600*temp[0] + 60*temp[1] + temp[2]

def timeVal2Str(tVal):
    hrs = tVal / 3600
    mins = (tVal - 3600*hrs) / 60
    secs = tVal - 3600*hrs - 60*mins
    return str(hrs).rjust(2,'0')+':'+\
            str(mins).rjust(2,'0')+':'+\
            str(secs).rjust(2,'0')

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.rstrip(): continue
    # 'test' represents the test case, do something with it
    time1,time2 = map(timeStr2Val,test.split())
    print timeVal2Str(abs(time2-time1))

test_cases.close()