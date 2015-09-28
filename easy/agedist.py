#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it
    age = int(test)

    if 0<=age<3:
        print 'Still in Mama\'s arms'
    elif 3<=age<5:
        print 'Preschool Maniac'
    elif 5<=age<12:
        print 'Elementary school'
    elif 12<=age<15:
        print 'Middle school'
    elif 15<=age<19:
        print 'High school'
    elif 19<=age<23:
        print 'College'
    elif 23<=age<66:
        print 'Working for the man'
    elif 66<=age<101:
        print 'The Golden Years'
    else:
        print "This program is for humans"

test_cases.close()