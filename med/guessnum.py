#!/usr/bin/env python

import sys

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        responses = line.split()
        low,high,guess = 0,int(responses.pop(0)),None

        for rsp in responses:
            guess = low+(high+1-low)/2
            if rsp == "Lower":
                high=guess-1
            elif rsp == "Higher":
                low=guess+1
            elif rsp == "Yay!":
                break
        print guess

if __name__ == "__main__":
    main(sys.argv[1])