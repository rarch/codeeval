#!/usr/bin/env python
import sys

def main():
    if sys.byteorder == "little":
        print "LittleEndian"
    else:
        print "BigEndian"

if __name__  == "__main__":
    main()