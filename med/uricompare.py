#!/usr/bin/env python

import sys
from string import hexdigits

DEFAULT_PORT=r':80'

def normalize_uri(uri):
    """ hacky, but seems to work """
    # get rid of hex
    res,uri=[],list(uri)
    while uri:
        c=uri.pop(0)
        if c==r'%':
            digs=''
            while uri[0] in hexdigits:
                digs+=uri.pop(0)
            if digs:
                c=chr(int(r'0x'+digs,16))
        res.append(c)

    # lower and check port
    prtcl,sep,uri_port_path=''.join(res).lower().partition(r'://')
    uri_port_path=uri_port_path.replace(DEFAULT_PORT,'').split(r'/')
    res=''.join([prtcl,sep,r'/'.join(uri_port_path)])
    return res

def main(filename):
    lines=[]
    with open(filename) as f_in: # get only nonempty lines
        lines = [line.strip() for line in f_in if line.rstrip()]

    for line in lines:
        [uri_a,uri_b]=line.split(';')
        print normalize_uri(uri_a)==normalize_uri(uri_b)

if __name__ == "__main__":
    main(sys.argv[1])