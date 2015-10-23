#!/usr/bin/env python
from __future__ import division
import sys
from operator import add,mul,sub,neg#,div
OpsDict={'-':(sub,2,'l'),'+':(add,2,'l'),'^':(pow,4,'r'),'/':(lambda x,y:x/y,3,'l'),
            '*':(mul,3,'l'),'(':(None,9,'l'),')':(None,0,'l'),
            'u':(neg,5,'r')} # 'u' is for unary minus

class ExprTree:
    def __init__(self,cargo,left=None,right=None):
        self.cargo=cargo
        self.left=left
        self.right=right
    def __str__(self):
        if None==self.cargo: return ''
        else:
            return str(self.cargo)+('('+\
                (str(self.left) if self.left else '')+\
                (','+str(self.right) if self.right else '')+')'
                    if (self.left or self.right) else '')
    def literal(self):
        res='ExprTree('
        if self.cargo:
            if str==type(self.cargo):
                res+='\''+str(self.cargo)+'\''
            else: res+=str(self.cargo)
            if self.left:
                res=res+','+self.left.literal()
                if self.right: res=res+','+self.right.literal()
        res+=')'
        return res
    def my_eval(self):
        global OpsDict
        if isinstance(self.cargo,(int,long,float,complex)):return self.cargo
        if 'u'==self.cargo: return OpsDict[self.cargo][0](self.left.my_eval())
        return OpsDict[self.cargo][0](self.left.my_eval(),self.right.my_eval())

def RPN2tree(tokens):
    stack=[]
    for tok in tokens:
        if tok not in OpsDict:
            stack.append(ExprTree(tok))
        elif 'u'==tok:
            stack.append(ExprTree(tok,stack.pop()))
        else:
            temp=stack.pop()
            stack.append(ExprTree(tok,stack.pop(),temp))
    return stack.pop()

def pprint(val,places=5):
    if float==type(val):
        val=round(val,places)
        if val.is_integer():
            val=int(val)
    return val

def parse(exprStr):
    global OpsDict
    res,buf=[],''
    for char in exprStr:
        if char.isdigit() or '.'==char:
            buf+=char
        if char in OpsDict:
            if buf:
                temp=float(buf)
                res+=[int(temp) if temp.is_integer() else temp]
                buf=''
            res+=('u' if '-'==char and (not res or res[-1] in OpsDict)
                else char)
    if buf:
        temp=float(buf)
        res+=[int(temp) if temp.is_integer() else temp]
    return res

def infix2postfix(infix):
    opstack,postfix=[],[]
    for tok in infix:
        if tok not in OpsDict:
            postfix.append(tok)
        else:
            if '('==tok:
                opstack.append(tok)
            elif ')'==tok:
                temp=opstack.pop()
                while '('!=temp:
                    postfix.append(temp)
                    temp=opstack.pop()
            elif (not opstack) or OpsDict[tok][1]>OpsDict[opstack[-1]][1]:
                opstack.append(tok)
            else:
                while opstack:
                    if '('==opstack[-1]: break
                    postfix.append(opstack.pop())
                opstack.append(tok)
    while opstack:
        postfix.append(opstack.pop())
    return postfix

def evalRPN(tokens):
    stack=[]
    for tok in tokens:
        if tok not in OpsDict:
            stack.append(tok)
        elif 'u'==tok:
            stack.append(OpsDict[tok][0](stack.pop()))
        else:
            temp = stack.pop()
            stack.append(OpsDict[tok][0](stack.pop(),temp))
    return stack.pop()

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        print pprint(evalRPN(infix2postfix(parse(line))))
        # print pprint(RPN2tree(infix2postfix(parse(line))).my_eval())


if __name__ == "__main__":
    main(sys.argv[1])
