#!/usr/bin/env python

import sys

def cmpr(ranka,rankb):
    def val(strng):
        if 'J'==strng:return 11
        elif 'Q'==strng:return 12
        elif 'K'==strng:return 13
        elif 'A'==strng:return 14
        else: return int(strng) 
    return (val(ranka[0])>val(rankb[0])) - (val(ranka[0])<val(rankb[0]))

def main(filename):
    pretty=lambda x:''.join(x)

    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        cards,trump = [x.strip() for x in line.split(' | ')]
        cards = [(card[:-1],card[-1]) for card in cards.split()]

        if cards[0][1]==trump and not cards[1][1]==trump:
            print pretty(cards[0])
        elif cards[1][1]==trump and not cards[0][1]==trump:
            print pretty(cards[1])
        else:
            c=cmpr(*cards)
            if 0<c: print pretty(cards[0])
            elif 0>c: print pretty(cards[1])
            else: print ' '.join([pretty(card) for card in cards])

if __name__ == "__main__":
    main(sys.argv[1])