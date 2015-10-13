#!/usr/bin/env python

import sys

def lockIters(locks,iters):
    unlocked = [True]*locks
    for _ in xrange(iters-1):
        for ind in xrange(1,locks):
            if (1==ind%2 and 2==ind%3):
                unlocked[ind] = True
            elif 1==ind%2:
                unlocked[ind] = False
            elif 2==ind%3:
                unlocked[ind] = not unlocked[ind]
    unlocked[-1] = not unlocked[-1]
    return unlocked.count(True)

# def lockIters(locks,iters):
#     unlocked = [True]*locks
#     for _ in xrange(iters-1):
#         for ind in xrange(1,locks,2):
#             unlocked[ind] = False
#         for ind in xrange(2,locks,3):
#             unlocked[ind] = not unlocked[ind]
#     unlocked[-1] = not unlocked[-1]

#     return unlocked.count(True)

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        [locks,iters]=map(int,line.split())
        print lockIters(locks,iters)

if __name__ == "__main__":
    main(sys.argv[1])