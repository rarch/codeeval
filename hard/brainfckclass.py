#!/usr/bin/env python

import sys

# WHAT IS WRONG WITH THIS? IT PRINTS THE GIVEN TESTS PROPERLY!
# +[--->++<]>+++.[->+++++++<]>.[--->+<]>----.
# ++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.
# Yo!
# Hello World!

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
    def run(self):
        while self.codePtr<len(self.code):
            self.execDict[self.code[self.codePtr]]()
            self.codePtr+=1
        sys.stdout.write(chr(10)) # print newline
    def incDPtr(self):
        self.dataPtr+=1
        if self.dataPtr==len(self.data):
            self.data+=bytearray(b'\x00')
    def decDPtr(self):
        if self.dataPtr>0:
            self.dataPtr-=1
        else:
            self.dataPtr=len(self.data)-1
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
            depth=0
            while 0<depth or self.code[self.codePtr]!=']':
                self.codePtr+=1
                if self.code[self.codePtr]=='[':
                    depth+=1
                if self.code[self.codePtr]==']':
                    depth-=1
    def goLeft(self):
        if self.data[self.dataPtr]!=0:
            depth=0
            while 0<depth or self.code[self.codePtr]!='[':
                self.codePtr-=1
                if self.code[self.codePtr]==']':
                    depth+=1
                if self.code[self.codePtr]=='[':
                    depth-=1

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines=[line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        mybrain=BrainFuck(line)
        mybrain.run()

if __name__ == "__main__":
    main(sys.argv[1])