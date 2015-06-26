#!/usr/bin/env python

import sys
# use lambda instead
# from operator import add, mul, div

def parse(line):
    opns = { '+' : lambda a,b: a+b,
             '*' : lambda a,b: a*b,
             '/' : lambda a,b: a/b }

    operands, operations = [],[]

    for token in line.strip().split():
        if token.isdigit():
            operands.append(float(token))
        else:
            operations.append(opns[token])

    # pop from end, so keep operations as is and reverse operands
    return operands[::-1], operations

def main():
    lines = []
    operands,operations = [],[]

    with open(sys.argv[1],'r') as fp:
        lines = fp.readlines()

    for line in lines:
        if line:
            operands, operations = parse(line)
            value = operands.pop()
    
            while operands and operations:
                value = operations.pop()(value, operands.pop())
    
            print int(value)

if __name__ == "__main__":
    main()
