#!/usr/bin/env python

import sys

months = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,\
            'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}

def parseDate(dateStr):
    month,year = dateStr.split(' ')
    return months[month]+12*int(year)

parsePair = lambda pair:map(parseDate,pair)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it

    ranges = map(lambda x:parsePair(tuple(x.split('-'))),test.split('; '))

    working = {} # not most effective; is there a simple arithmetic solution?
    for rng in ranges:
        # from start to finish (1st to 31st)
        for val in xrange(rng[0],rng[1]+1):
            working[val] = True
    duration = len(working)
    print duration/12

test_cases.close()