#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

the_last_digit = number % 10

format_text = "Last digit of {} is {} and is {}"
zero = "0"
greater_than_5 = "greater than 5"
less_than_6_and_not_0 = "less than 6 and not 0"

if the_last_digit > 5:
    print(format_text.format(number, the_last_digit, greater_than_5))
elif (the_last_digit < 6) and (the_last_digit) != 0:
    print(format_text.format(number, the_last_digit, less_than_6_and_not_0))
else:
    print(format_text.format(number, the_last_digit, zero))
