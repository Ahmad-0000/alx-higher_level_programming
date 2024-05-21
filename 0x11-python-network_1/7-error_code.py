#!/usr/bin/python3
'''A script that takes in a URL, fetches the URL and displays the body of the
response decoded in "utf-8" when no error is there, using "requests" module'''
import requests
import sys


url = sys.argv[1]
response = requests.get(url, timeout=2)
if response.status_code >= 400:
    print(f"Error code: {response.status_code}")
else:
    print(response.text)
