#!/usr/bin/env python

import sys

def getCity(cityStr):
    city,distStr = cityStr.strip().split(',')
    return (city,int(distStr))

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it
    cities = sorted(map(getCity,test.rstrip(';').split(';')), key = lambda x:x[1])
    dists = [item[1] for item in cities]
    length = len(dists)
    print ','.join(map(str,[dists[0]] + [dists[ind]-dists[ind-1] for ind in xrange(1,length)]))


test_cases.close()