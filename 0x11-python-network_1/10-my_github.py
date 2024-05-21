#!/usr/bin/python3
"""A script that takes a GitHub token and returns the associated user id"""
import requests
import sys


if __name__ == "__main__":
    token = sys.argv[1]
    headers = {"Authorization": f"Bearer {token}",
               "Accept": "application/json",
               "X-GitHub-Api-Version": "2022-11-28"}
    response = requests.post("https://api.github.com/user", headers=headers)
    print(response.json().get('id'))
