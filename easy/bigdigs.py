#!/usr/bin/env python

import sys

DIGS = ['-**----*--***--***---*---****--**--****--**---**--',
        '*--*--**-----*----*-*--*-*----*-------*-*--*-*--*-',
        '*--*---*---**---**--****-***--***----*---**---***-',
        '*--*---*--*-------*----*----*-*--*--*---*--*----*-',
        '-**---***-****-***-----*-***---**---*----**---**--',
        '--------------------------------------------------' ]
WIDTH = 5
LENDIGS = len(DIGS)

def digLine(line,val):
    ind = val*(WIDTH)
    return DIGS[line][ind:ind+WIDTH]

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it
    res,lim=['']*LENDIGS,len(test)
    for ind in xrange(lim):
        char = test[ind]
        if char.isdigit():
            val = int(char)

            for line in xrange(LENDIGS):
                res[line] = res[line]+digLine(line,val)

    print '\n'.join(res)

test_cases.close()