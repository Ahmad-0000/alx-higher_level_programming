#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    status = False
    try:
        print('{:d}'.format(value))
        status = True
    except Exception as e:
        print('Exception:', e, file=sys.stderr)
    finally:
        return status
