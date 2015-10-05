#!/usr/bin/env python

import sys

def initJumpMap(code):
    temp,mapping=[],{}
    for ind,char in enumerate(code):
        if char=='[':
            temp.append(ind)
        if char==']':
            start = temp.pop()
            mapping[start],mapping[ind] = ind,start
    return mapping

def brainfuck(codeStr):
    dataPtr,data,codePtr=0,bytearray(b'\x00'),0
    code=filter(lambda x:x in "><+-.,[]",codeStr)
    mapping=initJumpMap(code)

    while codePtr<len(code):
        cmd = code[codePtr]

        if cmd=='>': #< increment data pointer
            dataPtr+=1
            if dataPtr == len(data):
                data.append(b'\x00')
        if cmd=='<': #> decrement data pointer
            if dataPtr>0:
                dataPtr-=1
            else:
                data=bytearray(b'\x00')+data #expand left
        if cmd=='+': # increment data value
            data[dataPtr]=data[dataPtr]+0x01 if data[dataPtr]<0xff else 0x00
        if cmd=='-': # decrement data value
            data[dataPtr] = data[dataPtr]-0x01 if data[dataPtr]>0x00 else 0xff
        if cmd=='.': # putchar
            sys.stdout.write(chr(data[dataPtr]))
        if cmd==',': # readchar
            data[dataPtr]=sys.stdin.read(1)
        if cmd=='[': # go right to ] accounting for nests if 0
            if data[dataPtr]==0x00:
                codePtr=mapping[codePtr]
        if cmd==']': #] go left to [ accounting for nests if not 0
            if data[dataPtr]!=0x00:
                codePtr=mapping[codePtr]

        codePtr+=1 # move to next command
    sys.stdout.write(chr(10)) # print newline

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if not test.rstrip(): continue
    brainfuck(test)

test_cases.close()