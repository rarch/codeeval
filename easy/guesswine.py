#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.rstrip(): continue
    # 'test' represents the test case, do something with it
    [words,chars] = map(str.strip,test.split('|'))
    words = words.split()

    # result = ' '.join([word for word in words if
                    # all((ch in word) for ch in chars)])

    # result, occurrences = [], {}
    result = []

    # deal with duplicates
    for word in words:
        if all(chars.count(char) <= word.count(char) for char in chars):
            result.append(word)

    # for char in chars:
    #     if char in occurrences:
    #         occurrences[char] = occurrences[char] + 1
    #     else:
    #         occurrences[char] = 1

    # for word in words:
    #     if all(occurrences[char] <= word.count(char) for char in chars):
    #         result.append(word)

    print ' '.join(result) if result else False

test_cases.close()