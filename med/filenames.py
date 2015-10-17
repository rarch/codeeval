#!/usr/bin/env python

import sys,re

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        fnames = line.split()
        pattern = '^'+fnames.pop(0)+'$'
        # a period # any char any num times # any single char
        pattern = pattern.replace('.','[.]').replace('*','.*').replace('?','.')
        pattern = pattern.encode('string-escape')

        regex = re.compile(pattern)
        res = filter(regex.search,fnames)
        print ' '.join(res) if res else '-'

if __name__ == "__main__":
    main(sys.argv[1])