#!/usr/bin/env python

import sys

def getSpot(line):
    val = line.find('C')
    return val if val>0 else line.find('_')

test_case=[]
with open(sys.argv[1], 'r') as fp:
    test_case = fp.read().strip().splitlines()

path = {0:'|', -1:'/', 1:'\\'}

#first case
line = test_case[0]
last,comp,curr = None,None,getSpot(line)
print line.replace(line[curr], path[0]) 

#subsequent cases
for line in test_case[1:]:
    last,curr = curr,getSpot(line)
    comp = -1 if last > curr else 1 if last < curr else 0
    print line.replace(line[curr], path[comp])
