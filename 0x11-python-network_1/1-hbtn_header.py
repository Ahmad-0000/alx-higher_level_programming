#!/usr/bin/python3
"""A script takes in a URL and return the value of the header "X-Request-Id"
returned in the response messages"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header = response.info().get('X-Request-Id')
        print(header)
