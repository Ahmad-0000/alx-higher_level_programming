#!/usr/bin/python3
"""A script that takes in a URL and an email, uses a POST HTTP method to send
the email to the URL, then shows the response body using "requests" module"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    response = requests.get(url, params=email)
    print(response.text)
