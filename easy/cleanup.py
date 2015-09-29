#!/usr/bin/env python

import sys
from string import letters

translate = dict(zip(letters,letters[0:26]*2))

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it

    results,word = [],''
    for char in test: # go through all chars
        if char in letters: # char is alphabetical
            if not word: # new word, so add new spot in list of words
                results.append([])
                word = translate[char] # add corresp lower case letter
            else:
                word = word + translate[char]
        elif word: # whitespace, number or punctuation, and have not pushed last word yet
            results[-1],word = word,'' # append word, delete stored
    
    if word: # if test string ended with word rather than whitespace/punctuation/digit
        results[-1]=word

    print ' '.join(results) # join all lowercase words with single space

test_cases.close()