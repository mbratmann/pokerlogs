#!/usr/bin/env python

filename = 'C:\\Users\\marcb\\Documents\\888poker.de\\HandHistory\\MrBeeeeee\\888.de20240318 Babrujsk $0.01-$0.02 No Limit Holdem.txt'

def main():
    f = open(filename, "r")
    for line in f:
        if line.startswith("#Game No : "):
            print(line)

if __name__ == "__main__":
    main()