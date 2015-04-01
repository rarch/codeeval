#!/usr/bin/env python
import sys

def main():
    if "little" == sys.byteorder:
        print "LittleEndian"
    else:
        print "BigEndian"

if __name__  == "__main__":
    main()