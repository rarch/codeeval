#!/usr/bin/env python

import sys

WIDTH=80

def lessThanWidth(lst):
    global WIDTH
    line=[lst.pop(0)]
    while lst and len(line)+len(lst[0])+sum([len(elt) for elt in line])<=WIDTH:
        line.append(lst.pop(0))
    return [line,lst]

def justifyLines(lines):
    output=[' '.join(lines.pop())] # last line
    while lines:
        temp=lines.pop()
        length = sum([len(word) for word in temp])+len(temp)-1
        while length<WIDTH:
            for ind in xrange(len(temp)-1):
                temp[ind]=temp[ind]+' '
                length+=1
                if length==WIDTH: break
        output.insert(0,' '.join(temp))
    return '\n'.join(output)

def main(filename):
    global WIDTH
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        words,lstsOfWords = line.split(),[]
        while words:
            [lst,words]=lessThanWidth(words)
            lstsOfWords.append(lst)

        print justifyLines(lstsOfWords)

if __name__ == "__main__":
    main(sys.argv[1])
    