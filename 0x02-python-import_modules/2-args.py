#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

n = len(sys.argv) - 1

if n == 0:
    print("{:d} arguments.".format(n))
elif n == 1:
    print("{:d} argument:".format(n))
    print("{:d}: {:s}".format(n, sys.argv[1]))
else:
    print("{:d} arguments:".format(n))
    for i in range(1, n + 1):
        print("{:d}: {:s}".format(i, sys.argv[i]))
