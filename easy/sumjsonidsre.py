#!/usr/bin/env python

import sys
import re

item = '[{[^}]*\"id\": (-?\d+)[^}]*\"label\": \"[^\"]*\"}[, ]?]*'
regex = re.compile(item)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it

    results = re.findall(regex,test)
    print reduce(lambda a,b:a+int(b),results,0)

test_cases.close()