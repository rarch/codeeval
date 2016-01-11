#!/usr/bin/env python

import sys

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        prefd={}
        for country,supports in enumerate(line.split('|'),start=1):
            for team in supports.strip().split():
                prefd[team]=prefd.get(team,[])+[str(country)]
        
        keys=prefd.keys()
        keys.sort(key=int)

        output=''
        for key in keys:
            countries=prefd[key]
            countries.sort(key=int)

            output+=key+':'+','.join(countries)+'; '

        print output[:-1]

if __name__ == "__main__":
    main(sys.argv[1])