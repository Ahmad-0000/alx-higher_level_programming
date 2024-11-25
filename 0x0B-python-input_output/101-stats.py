#!/usr/bin/python3
"""
Log Parsing
"""
import sys


i = 0
so_far_size = 0
code_time = {code: 0 for code in ["200", "301", "400",
                                  "401", "403", "404",
                                  "405", "500"]}

for line in sys.stdin:
    so_far_size += int(line.split(' ')[-1])
    code_time[line.split()[-2]] += 1
    i += 1
    if i == 10:
        print('File size:', so_far_size)
        so_far_size = 0
        for _ in sorted(code_time.keys()):
            print(f'{_}: {code_time[_]}')
        i = 0
        code_time.update({code: 0 for code in ["200", "301", "400",
                                               "401", "403", "404",
                                               "405", "500"]})
