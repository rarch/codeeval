#!/usr/bin/env python

import sys

codel = {'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c',\
        'g':'v','h':'x',\
        'i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k',\
        'p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p',\
        'w':'f','x':'m','y':'a','z':'q'}

# from string import lowercase
# print ''.join([elt if elt not in codel.values() else '' for elt in lowercase])

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.rstrip(): continue
    # 'test' represents the test case, do something with it
    print ''.join([char if ' '==char else codel[char] for char in test.strip()])

test_cases.close()