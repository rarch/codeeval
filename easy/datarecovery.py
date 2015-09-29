#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it
    split_ = lambda x:x.split()
    words,inds = map(split_, test.split(';'))
    inds = map(lambda x:int(x)-1,inds)

    for ind in xrange(0,len(words)):
        if ind not in inds:
            inds.append(ind)

    lookup = {}
    for ind in xrange(len(inds)):
        lookup[inds[ind]] = words[ind]
    
    length = len(lookup)
    print ' '.join([lookup[key] for key in xrange(0,length)]).strip()

test_cases.close()