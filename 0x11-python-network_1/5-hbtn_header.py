#!/usr/bin/python3
"""A script takes in a URL and return the value of the header "X-Request-Id"
returned in the response messages using "requests" module"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
