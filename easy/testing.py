#!/usr/bin/env python

import sys

def test(bugs):
    if bugs==0: return 'Done'
    elif bugs<=2: return 'Low'
    elif bugs<=4: return 'Medium'
    elif bugs<=6: return 'High'
    else: return 'Critical'

def getBugs(str1,str2):
    count=0
    for ind in xrange(len(str1)):
        if str1[ind]!=str2[ind]: count+=1
    return count

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        print test(getBugs(*(line.split(' | '))))

if __name__ == "__main__":
    main(sys.argv[1])