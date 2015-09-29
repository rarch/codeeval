#!/usr/bin/env python

import sys

digdict={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it
    
    words,res = test.split(';'),''
    for word in words:
        res = res+digdict[word]
    print res

test_cases.close()