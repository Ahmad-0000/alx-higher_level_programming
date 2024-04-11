#!/usr/bin/python3

i = -11

for j in range(122, 96, -1):
    i += 1
    print("{}".format(chr(j - (32 * (i % 2)))), end="")
