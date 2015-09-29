#!/usr/bin/env python

import sys
import json

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if not test: continue
    # 'test' represents the test case, do something with it
    total = 0
    parsed_json = json.loads(test)
    for item in parsed_json[unicode('menu')][unicode('items')]:
        if item and unicode('label') in item:
            total = total + item[unicode('id')]
    print total

test_cases.close()