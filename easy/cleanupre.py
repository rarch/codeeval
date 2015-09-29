#!/usr/bin/env python

import sys
import re
from string import letters,maketrans

table = maketrans(letters[26:],letters[:26])

translate = dict(zip(letters,letters[:26]*2))

item = '([a-zA-Z]+)'
regex = re.compile(item)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it
    results = re.findall(regex,test)

    print ' '.join([word.translate(table) for word in results])
    # print ' '.join(results) # join all lowercase words with single space

test_cases.close()