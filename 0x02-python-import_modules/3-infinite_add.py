#!/usr/bin/python3
import sys

if __name__ == "__main__":
    n = len(sys.argv) - 1
    result = 0
    if n == 0:
        print("0")
    else:
        for i in range(1, n+1):
            result = result + int(sys.argv[i])
        print(result)
