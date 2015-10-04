#!/usr/bin/env python

import sys
import re

# ONLY PARTIAL SOLUTION. WHAT IS WRONG WITH THIS REGEX? WHICH EDGE CASE?

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        email=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if not re.match(email,line):
            print "false"
        else:
            print "true"

if __name__ == "__main__":
    main(sys.argv[1])