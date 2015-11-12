#!/usr/bin/env python

import sys

def eratosthenes():
    D = {}
    val = 2
    while True:
        if not val in D:
            yield val
            D[val*val] = [val]
        else:
            for nxt in D[val]:
                D.setdefault(val+nxt,[]).append(nxt)
            del D[val]
        val+=1

primes = eratosthenes()
print sum(list([next(primes) for ind in xrange(1000)]))