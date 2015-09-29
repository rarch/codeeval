#!/usr/bin/env python

import sys
from string import uppercase as uppers,digits

# morse A-Z0-9
morseLtrs = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--',\
    '-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
morseDigs = ['-----','.----','..---','...--','....-','.....','-....','--...','---..','----.'] 

morse,plain = morseLtrs+morseDigs,uppers+digits
morseD = dict(zip(morse,plain))

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.rstrip(): continue
    # 'test' represents the test case, do something with it
    words = map(lambda x:x.split(),test.split('  '))
    print ' '.join([''.join(morseD[letter] for letter in word) for word in words])

test_cases.close()