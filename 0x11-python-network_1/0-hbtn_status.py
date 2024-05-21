#!/usr/bin/python3
"""A script to fetch "https://alx-intranet.hbtn.io/status" resorece"""
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as response:
        print("Body response:")
        print(f"\t- type: {type(response.read())}")
        print(f"\t- content: {response.read()}")
        print(f"\t- urf8 content: {response.read().decode('utf-8')}")

