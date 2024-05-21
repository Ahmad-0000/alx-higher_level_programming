#!/usr/bin/python3
"""A script to fetch "https://alx-intranet.hbtn.io/status" resorece"""
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- urf8 content: {content.decode('utf-8')}")

