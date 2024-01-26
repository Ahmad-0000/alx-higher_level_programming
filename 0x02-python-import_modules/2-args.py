#!/usr/bin/python3
import sys

length = len(sys.argv)
single_or_plural = ""
if length > 2:
    single_or_plural = 's'
if __name__ == "__main__":
    if length == 1:
        print("0 arguments.")
    else:
        print(f"{length - 1} argument{single_or_plural}:")
        for i in range(1, length):
            print(f"{i}: {sys.argv[i]}")
