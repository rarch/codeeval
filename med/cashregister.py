#!/usr/bin/env python

import sys

Currency = {'PENNY': .01,       'NICKEL': .05,
            'DIME': .10,        'QUARTER': .25,
            'HALF DOLLAR': .50, 'ONE': 1.00,
            'TWO': 2.00,        'FIVE': 5.00,
            'TEN': 10.00,       'TWENTY': 20.00,
            'FIFTY': 50.00,     'ONE HUNDRED': 100.00 }

scale = lambda x:int(100*x)
helper = lambda elt:[elt[0],scale(elt[1])]

def wordChange(amt):
    chng=[]
    for name,val in sorted([helper(elt) for elt in Currency.items()],
      key=lambda x:x[1],reverse=True):
        for ind in xrange(amt/val):
            chng.append(name)
            amt-=val
    return chng

def till(price,paid):
    price,paid = round(price,2),round(paid,2)
    if price>paid: return 'ERROR'
    elif price==paid: return 'ZERO'
    else:
        return ','.join(wordChange(scale(paid)-scale(price)))

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        pp,ch = [float(elt) for elt in line.split(';')]
        print till(pp,ch)

if __name__ == "__main__":
    main(sys.argv[1])