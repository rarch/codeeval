#!/usr/bin/env python

import sys
import re

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    email = re.compile(r"(^\"[^\"]+\"|[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

    for line in lines:
        print "true" if email.match(line) else "false"

if __name__ == "__main__":
    main(sys.argv[1])