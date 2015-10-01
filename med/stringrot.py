#!/usr/bin/env python

import sys

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        [str1,str2]=line.split(',')

        if len(str1)!=len(str2):
            print False; continue

        isRot,ind,length=False,0,len(str1)
        while not isRot and ind<length:
            if str1==str2[ind:]+str2[0:ind]:
                isRot=True
            ind+=1
        print isRot

if __name__ == "__main__":
    main(sys.argv[1])