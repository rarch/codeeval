#!/usr/bin/env python

from math import sqrt

def eratosthenes(n):
    """sieve of eratosthenes"""
    sieve = [True] * n

    lim = int(sqrt(n))

    for i in xrange(3,lim+1,2):
        if sieve[i]:
            sieve[i*i::i] = [False]*len(sieve[i*i::i])
    return [2]+[i for i in xrange(3,n,2) if sieve[i]]

def main():
    ispal = lambda n: str(n) == str(n)[::-1]

    LIM = 1001
    primes = eratosthenes(LIM)[::-1]

    for p in primes:
        if ispal(p):
            print p
            break
    
if __name__ == "__main__":
    main()