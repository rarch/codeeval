#!/usr/bin/env python

import sys

# reqs={'0':'11111100','1':'01100000','2':'11011010',
#       '3':'11110010','4':'01100110','5':'10110110',
#       '6':'10111110','7':'11100000','8':'11111110',
#       '9':'11110110' }
reqs={'1': 96, '0': 252, '3': 242, '2': 218, '5': 182,
      '4': 102, '7': 224, '6': 190, '9': 246, '8': 254}

def binInt(bitstr):
  """parse binary string to int"""
  return int(bitstr,2)

def getInt(nstr):
  """assume string of digits and decimal point"""
  global reqs
  if not '.' in nstr: # no decimal so it's easy
    return [reqs[c] for c in nstr]
  elif '.' == nstr[0]: # decimal has to trail, so add extra char
    return [1]+[reqs[c] for c in nstr[1:]]
  else: # find it
    res=[]
    for c in nstr:
      if c == '.':
        res[-1]+=1
      else:
        res.append(reqs[c])
    return res

def isValid(light,charout):
  return (light & charout)==charout

def scan(lights,strnum):
  length=len(lights)
  window=len(strnum)
  if length<window:return 0

  for start in xrange(length-window+1): # move start through list
    valid=True
    for ind in xrange(window): # move mark through window
      if not isValid(lights[start+ind],strnum[ind]):
        valid=False
        break # fail, change start
    if valid:
      return 1
  return 0

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        lights,my_str=line.split(';')
        
        int_lights=map(binInt,lights.split(' '))
        int_str=getInt(my_str)

        print scan(int_lights,int_str)

if __name__ == "__main__":
    main(sys.argv[1])
