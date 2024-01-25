#!/usr/bin/python3
import sys

total = 0
length = len(sys.argv)
if __name__ == "__main__":
    for i in range(1, length):
        total += int(sys.argv[i])
    print(total)
