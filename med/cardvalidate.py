#!/usr/bin/env python

import sys

def luhnCheck(cardStrNum):
    res,flag=0,False
    for char in cardStrNum[::-1]:
        if flag:
            temp = int(char)
            # 5*2=10->1; 6*2=12->3; 7*2=14->5. Nums LT 5 are ok, others 2x-9
            res = (res+2*temp if temp<5 else res+2*temp-9)
        else:
            res+=int(char)
        flag = not flag
    return (res%10==0)

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        print (1 if luhnCheck(line.replace(' ','')) else 0)

if __name__ == "__main__":
    main(sys.argv[1])