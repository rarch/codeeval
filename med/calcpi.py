#!/usr/bin/env python

import sys

# based on paper
# https://www.cs.ox.ac.uk/jeremy.gibbons/publications/spigot.pdf

def calc_pi(loc):
    def spigot():
        q,r,t,k,n,el=1,0,1,1,3,3
        while True:
            if 4*q+r-t<n*t:
                yield n
                n,q,r = ((10*(3*q+r))/t)-10*n,10*q,10*(r-n*t)
            else:
                q,t,el,k,n,r=q*k,t*el,el+2,k+1,(q*(7*k)+2+(r*el))/(t*el),(2*q+r)*el
    i=1
    for dig in spigot():
        if i==loc: return dig
        i+=1


def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        print calc_pi(int(line))

if __name__ == "__main__":
    main(sys.argv[1])