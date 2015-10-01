#!/usr/bin/env python

import sys

# val is 0 => 0; return 0
# val is 1 => 01; subtract 2^0; look at 0, return 0+count=0+1=1 and %3
# val is 2 => 0112; subtract 2^1; look at 0, return 0+count=0+1=1 and %3
# val is 3 => 0112; subtract 2^1; look at 1, return 1+count=1+1=2 and %3

def predictVal2(val):
    if val==0:return 0
    
    elt=1
    while elt<=val:
        elt*=2
    elt/=2
    return (1+predictVal(val-elt))%3

def predictVal1(val): # WHY IS THIS NOT WORKING? #
    if val<2:return val
    return (1+predictVal1(int("{0:b}".format(val)[1:],2)))%3

def predictVal(val):
    # is it that easy? IT IS THAT EASY
    return "{0:b}".format(val).count('1')%3

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        val = int(line)
        print predictVal(val)
        
if __name__ == "__main__":
    main(sys.argv[1])