#!/usr/bin/env python

import sys

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        links = {}
        duplicate=False
        for link in line.split(';'):
            temp=link.split('-')
            if temp[0] not in links:
                links[temp[0]]=temp[1]
            else: duplicate=True; break

        if ('END' not in links.values()) or\
          ('BEGIN' not in links.keys()) or duplicate:
            print 'BAD';continue

        chain=['BEGIN']
        temp=chain[-1]
        while len(chain)<len(links)+1 and 'END'!=temp:
            temp=links[temp]
            chain.append(temp)
        print ('GOOD' if ('END'==temp and len(chain)==len(links)+1) else 'BAD')

if __name__ == "__main__":
    main(sys.argv[1])