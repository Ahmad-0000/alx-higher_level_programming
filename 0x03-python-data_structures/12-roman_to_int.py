#!/usr/bin/python3

roman_int = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }


def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0
    i = 0
    total = 0
    while True:
        sybmol = roman_string[i]
        if i + 1 == len(roman_string):
            total += roman_int[symbol]
            return total
        if roman_int[symbol] < roman_int[roman_string[i + 1]]:
            total -= roman_int[symbol]
        else:
            total += roman_int[sybmol]
        i += 1
    return total
