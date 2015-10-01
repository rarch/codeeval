#!/usr/bin/env python

import sys

def josephus(n,m):
    people,res = [ind for ind in xrange(n)],[]

    ind,count = 0,len(people)
    while people:
        # modulus makes it circular
        # add m-1 rather than m, because you're popping somebody off every time
        #   therefor list is diminishing in size
        ind = (ind+m-1)%count
        res,count = res+[people.pop(ind)],count-1

    return res

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        [n,m] = map(int,line.split(','))
        res = josephus(n,m)
        print ' '.join([str(val) for val in res])

if __name__ == "__main__":
    main(sys.argv[1])