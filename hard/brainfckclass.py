#!/usr/bin/env python

# Yo!
# Hello World!
# 141201213012321312012321321321021321321321
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
# 33e
# 34b?
# QSnOIP6sp1A
# Just another brainfuck hacker
# Hello World!
# 0d7p
# TNGUSGnfKQrp4
# This is codeval.com

import sys

class BrainFuck:
    import sys
    def __init__(self,code=''):
        self.dataPtr=0
        self.data=bytearray(b'\x00')
        self.code=code
        self.codePtr=0
        self.execDict={ '>':self.incDPtr, '<':self.decDPtr,
                        '+':self.incDVal, '-':self.decDVal,
                        '.':self.putC,    ',':self.getC,
                        '[':self.goRight, ']':self.goLeft  }
        self.mapping = {}
        self.initJumpMap()
    def initJumpMap(self):
        temp=[]
        for ind,char in enumerate(self.code):
            if char=='[':
                temp.append(ind)
            if char==']':
                start = temp.pop()
                self.mapping[start],self.mapping[ind] = ind,start
    def run(self):
        while self.codePtr<len(self.code):
            self.execDict[self.code[self.codePtr]]()
            self.codePtr+=1
        sys.stdout.write(chr(10)) # print newline
    def incDPtr(self):
        self.dataPtr+=1
        if self.dataPtr==len(self.data):
            self.data.append(b'\x00')
    def decDPtr(self):
        if self.dataPtr:
            self.dataPtr-=1
        else:
            self.data=bytearray(b'\x00')+self.data #expand left
    def incDVal(self):
        if self.data[self.dataPtr]<0xff:
            self.data[self.dataPtr]+=0x01
        else:
            self.data[self.dataPtr]=0x00
    def decDVal(self):
        if self.data[self.dataPtr]>0x00:
            self.data[self.dataPtr]-=0x01
        else:
            self.data[self.dataPtr]=0xff
    def putC(self):
        sys.stdout.write(chr(self.data[self.dataPtr]))
    def getC(self):
        self.data[self.dataPtr]=sys.stdin.read(1)
    def goRight(self):
        if self.data[self.dataPtr]==0x00:
            self.codePtr=self.mapping[self.codePtr]
    def goLeft(self):
        if self.data[self.dataPtr]:
            self.codePtr=self.mapping[self.codePtr]

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines=[line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        mybrain=BrainFuck(filter(lambda x:x in "><+-.,[]",line))
        mybrain.run()

if __name__ == "__main__":
    main(sys.argv[1])