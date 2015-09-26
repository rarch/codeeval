#!/usr/bin/env python

import sys

def factors(n):
    # iterate up to sqrt, add i and n/i to list of factors; sort into list
    return sorted(list(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))))

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.rstrip(): continue
    # 'test' represents the test case, do something with it
    
    test = test.strip()
    # if it repeats all the way, length of substr must be factor of total length
    lengths = factors(len(test))

    for length in lengths:
        if all('' == spl for spl in test.split(test[0:length])):
            print length
            break