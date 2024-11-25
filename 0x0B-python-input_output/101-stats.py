#!/usr/bin/python3
"""
Log Parsing
"""
import sys


i = 0
code_time = {code: 0 for code in ["200", "301", "400",
                                  "401", "403", "404",
                                  "405", "500"]}
output = [0]
for line in sys.stdin:
    output[0] += int(line.split(' ')[-1])
    code_time[line.split()[-2]] += 1
    i += 1
    if i == 10:
        print('File size:', output[0])
        for _ in sorted(code_time.keys()):
            if code_time[_] != 0:
                print(f'{_}: {code_time[_]}')
        code_time.update({code: 0 for code in ["200", "301", "400",
                                               "401", "403", "404",
                                               "405", "500"]})
        output = [0]
        i = 0

if output[0]:
    print('File size:', output[0])
    for _ in sorted(code_time.keys()):
        if code_time[_] != 0:
            print(f'{_}: {code_time[_]}')
