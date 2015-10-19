#!/usr/bin/env python

import sys

State=None
Key=''
Text=''
Key_len=0
Txt_len=0

# def pprint(arr2d):
#     print'\n'.join([''.join([('1'if elt else '0')
#         for elt in row]) for row in arr2d])

# 0-> A* ; 1-> A*|B*
def matching(keyC,txt):
    if keyC and txt:
        return ('B' not in txt) or ('1'==keyC and ('A' not in txt))
    return False

def solve(row,p):
    global State,Key,Text,Key_len,Txt_len
    if State[-1][-1]: return # have valid soln
    if row==Key_len-1: # last elt in key, so solve
        State[-1][-1]=matching(Key[row],Text[p:])
        return
    # step through, starting next symbol where last ended
    for q in xrange(p,Txt_len-Key_len+row+1):
        if not State[row][q]: # next is not true yet
            # so increase substring until failure
            if not matching(Key[row],Text[p:q+1]): break
            State[row][q]=True
            solve(row+1,q+1)

def main(filename):
    global State,Key,Text,Key_len,Txt_len
    call_It=lambda cnd:"Yes" if cnd else "No"

    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        Key,Text=line.split()
        Key_len,Txt_len=len(Key),len(Text)

        # Text is too short, or key or text is empty
        if Key_len>Txt_len or ''==Key or ''==Text:
            print "No";continue
        if Key_len==1: # length one, so solve
            print call_It(matching(Key,Text));continue

        # Initialize State for dynamic solution
        State=[row[:] for row in [[False]*Txt_len]*Key_len]
        solve(0,0)

        print call_It(State[-1][-1])

if __name__ == "__main__":
    main(sys.argv[1])

# def checkSeq(binary,abSeq):
#     # ran out of time
#     seq = "^"
#     for char in binary:
#         if char=='0':seq+="A+"
#         if char=='1':seq+="(A+|B+)"
#     return ("Yes" if re.match(seq+"$",abSeq) else "No")

# def substrify(word):
#     res,last=[word[0]],word[0]
#     for char in word[1:]:
#         if char==last:
#             res[-1]+=char
#         else:
#             res+=[char]
#             last=char    
#     return res

# def verifyWithOpts(word,optnsLst):
#     """verify word against options list"""
#     """every substring in word must start with corresponding substring in option"""
#     subsWord=substrify(word)
#     subsOptsLst=map(substrify,optnsLst)

#     length=len(subsWord)
#     for subsOpt in subsOptsLst:
#         if len(subsOpt)!=length or subsWord[0][0]!=subsOpt[0][0] or\
#             subsWord[-1][0]!=subsOpt[-1][0]:
#             continue
#         for ind in xrange(length):
#             if not subsOpt[ind] in subsWord[ind]: # substring not found
#                 break
#             if (ind==length-1) and (subsOpt[ind] in subsWord[ind]):
#                 return True # got through word, and found it
#     return False

# def checkLetters(digs,letters):
#     options = ['']
#     for dig in digs:
#         if dig=='0':
#             options = [optn+'A' for optn in options]
#         else:
#             options = reduce(list.__add__,[[optn+'A',optn+'B'] for optn in options])
#     return verifyWithOpts(letters,options)