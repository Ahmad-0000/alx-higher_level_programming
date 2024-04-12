#!/usr/bin/python3
import sys
import calculator_1

if (len(sys.argv) != 4):
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

op = sys.argv[2]

if (op != '+' and op != '-' and op != '*' and op != '/'):
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

first_num = int(sys.argv[1])
second_num = int(sys.argv[3])

op_fun_pairs = {'+': calculator_1.add,
                '-': calculator_1.sub,
                '*': calculator_1.mul,
                '/': calculator_1.div}

for i in op_fun_pairs.keys():
    if op == i:
        print(op_fun_pairs[f'{op}'](first_num, second_num))
        break
