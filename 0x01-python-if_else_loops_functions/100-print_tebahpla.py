#!/usr/bin/python3

i = 0

for j in range(122, 96, -1):
    i += 1
    if i % 2 == 0:
        print(chr(j - 32), end="")
    else:
        print(chr(j), end="")
