#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it
    upper = lower = 0
    for char in test:
        val = ord(char)
        if 65<=val<91:
            upper = upper + 1
        elif 97<=val<123:
            lower = lower + 1    
    total = upper + lower

    percentage = lambda x,y:100.00*float(x)/float(y)

    print "lowercase: %.2f uppercase: %.2f" % (\
            float(percentage(lower,total)),\
            float(percentage(upper,total)))
        

test_cases.close()